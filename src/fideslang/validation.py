"""
Contains all of the additional validation for the resource models.
"""
import re
from collections import Counter
from typing import Dict, Generator, List, Optional, Pattern, Set, Tuple
from typing_extensions import Annotated

from packaging.version import Version
from pydantic import StringConstraints, ValidationInfo
from pydantic_core import core_schema


class FidesValidationError(ValueError):
    """Custom exception for when the pydantic ValidationError can't be used."""


class FidesVersion(Version):  # TODO what is the best way to define this class?
    """Validate strings as proper semantic versions."""

    @classmethod
    def __get_pydantic_core_schema__(cls, source, handler) -> core_schema.CoreSchema:
        return core_schema.no_info_after_validator_function(cls.validate)

    @classmethod
    def validate(cls, value: str) -> Version:
        """Validates that the provided string is a valid Semantic Version."""
        if isinstance(value, str):
            return Version(value)
        return value


class FidesKey(str):  # TODO - what is the best way to create this custom str type?
    """
    A FidesKey type that creates a custom constrained string.
    """

    @classmethod
    def __get_pydantic_core_schema__(cls, source, handler) -> core_schema.CoreSchema:
        return core_schema.with_info_before_validator_function(
            cls.validate, handler(str), field_name=handler.field_name
        )

    regex: Pattern[str] = re.compile(r"^[a-zA-Z0-9_.<>-]+$")

    @classmethod  # This overrides the default method to throw the custom FidesValidationError
    def validate(cls, value: str, _: Optional[ValidationInfo] = None) -> str:
        """Throws ValueError if val is not a valid FidesKey"""
        # TODO previously FidesKey would coerce to a string if it could, but with Pydantic,
        # that's not the pattern. How should we approach here?
        try:
            value = str(value)
        except ValueError:
            raise Exception("Cannot coerce to string")

        if not cls.regex.match(value):
            raise FidesValidationError(
                f"FidesKeys must only contain alphanumeric characters, '.', '_', '<', '>' or '-'. Value provided: {value}"
            )

        return value


def sort_list_objects_by_name(values: List) -> List:
    """
    Sort objects in a list by their name.
    This makes resource comparisons deterministic.
    """
    values.sort(key=lambda value: value.name)
    return values


def unique_items_in_list(values: List) -> List:
    """
    Verify that the `name` attributes of each item in the provided list are unique.

    This is useful for fields where there is no FidesKey but we want to
    do a uniqueness check.
    """
    names = [item.name for item in values]
    duplicates: Dict[str, int] = {
        name: count for name, count in Counter(names).items() if count > 1
    }
    if duplicates:
        raise FidesValidationError(
            f"Duplicate entries found: [{','.join(duplicates.keys())}]"
        )

    return values


def no_self_reference(value: FidesKey, values: ValidationInfo) -> FidesKey:
    """
    Check to make sure that the fides_key doesn't match other fides_key
    references within an object.

    i.e. DataCategory.parent_key != DataCategory.fides_key
    """
    fides_key = FidesKey.validate(values.data.get("fides_key", ""))
    if value == fides_key:
        raise FidesValidationError("FidesKey can not self-reference!")
    return value


def deprecated_version_later_than_added(
    version_deprecated: Optional[FidesVersion], values: ValidationInfo
) -> Optional[FidesVersion]:
    """
    Check to make sure that the deprecated version is later than the added version.

    This will also catch errors where the deprecated version is defined but the added
    version is empty.
    """

    if not version_deprecated:
        return None

    version_added = values.data.get("version_added")
    version_added = FidesVersion(version_added) if version_added else Version("0")
    # Why is version_deprecated a string here and not already a FidesVersion?
    version_deprecated = FidesVersion(version_deprecated)

    if version_deprecated < version_added:
        raise FidesValidationError(
            "Deprecated version number can't be earlier than version added!"
        )

    if version_deprecated == version_added:
        raise FidesValidationError(
            "Deprecated version number can't be the same as the version added!"
        )
    return version_deprecated


def has_versioning_if_default(is_default: bool, values: ValidationInfo) -> bool:
    """
    Check to make sure that version fields are set for default items.
    """

    # If it's a default item, it at least needs a starting version
    if is_default:
        try:
            assert values.data.get("version_added")
        except AssertionError:
            raise FidesValidationError("Default items must have version information!")
    # If it's not default, it shouldn't have version info
    else:
        try:
            assert not values.data.get("version_added")
            assert not values.data.get("version_deprecated")
            assert not values.data.get("replaced_by")
        except AssertionError:
            raise FidesValidationError(
                "Non-default items can't have version information!"
            )

    return is_default


def is_deprecated_if_replaced(replaced_by: str, values: ValidationInfo) -> str:
    """
    Check to make sure that the item has been deprecated if there is a replacement.
    """

    if replaced_by and not values.data.get("version_deprecated"):
        raise FidesValidationError("Cannot be replaced without deprecation!")

    return replaced_by


def matching_parent_key(parent_key: FidesKey, values: ValidationInfo) -> FidesKey:
    """
    Confirm that the parent_key matches the parent parsed from the FidesKey.
    """

    fides_key = FidesKey.validate(values.data.get("fides_key", ""))
    split_fides_key = fides_key.split(".")

    # Check if it is a top-level resource
    if len(split_fides_key) == 1 and not parent_key:
        return parent_key

    # Reform the parent_key from the fides_key and compare
    parent_key_from_fides_key = ".".join(split_fides_key[:-1])
    if parent_key_from_fides_key != parent_key:
        raise FidesValidationError(
            "The parent_key ({0}) does match the parent parsed ({1}) from the fides_key ({2})!".format(
                parent_key, parent_key_from_fides_key, fides_key
            )
        )
    return parent_key


def parse_data_type_string(type_string: Optional[str]) -> Tuple[Optional[str], bool]:
    """Parse the data type string. Arrays are expressed in the form 'type[]'.

    e.g.
    - 'string' -> ('string', false)
    - 'string[]' -> ('string', true)

    These data_types are for use in DatasetField.fides_meta.
    """
    if not type_string:
        return None, False
    idx = type_string.find("[]")
    if idx == -1:
        return type_string, False
    return type_string[:idx], True


# Data types that Fides is currently configured to handle
DATA_TYPE_NAMES: Set[str] = {
    "string",
    "integer",
    "float",
    "boolean",
    "object_id",
    "object",
}


def is_valid_data_type(type_name: str) -> bool:
    """Is this type a valid data type identifier in fides?"""
    return type_name is None or type_name in DATA_TYPE_NAMES


def valid_data_type(data_type_str: Optional[str]) -> Optional[str]:
    """If the data_type is provided ensure that it is a member of DataType."""

    parsed_date_type, _ = parse_data_type_string(data_type_str)
    if not is_valid_data_type(parsed_date_type):  # type: ignore
        raise ValueError(f"The data type {data_type_str} is not supported.")

    return data_type_str
