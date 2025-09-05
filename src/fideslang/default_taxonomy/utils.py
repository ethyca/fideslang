from typing import Dict, Optional, Type, Union
from dataclasses import dataclass

from fideslang.models import DataCategory, DataSubject, DataUse


@dataclass
class CheckDeprecationResult:
    """Result of checking a fides_key for deprecation."""

    original_key: str
    is_deprecated: bool
    replacement_key: Optional[str] = None

    @property
    def fides_key(self) -> str:
        """Get the fides_key that should be used (replacement if deprecated, original if not)."""
        return (
            self.replacement_key
            if self.is_deprecated and self.replacement_key
            else self.original_key
        )


CustomType = Union[DataCategory, DataSubject, DataUse]


def default_factory(taxonomy_class: CustomType, **kwargs: Dict) -> CustomType:
    """
    Generate default taxonomy objects.

    Given that we know these are defaults, set default values accordingly.
    """

    kwargs["is_default"] = True  # type: ignore[assignment]

    if not kwargs.get("version_added"):
        # This is the version where we started tracking from, so
        # we use it as the default starting point.
        kwargs["version_added"] = "2.0.0"  # type: ignore[assignment]
    item = taxonomy_class.model_validate(kwargs)
    return item


def check_for_deprecated_default_fides_key(
    taxonomy_class: Type[CustomType], fides_key: str
) -> CheckDeprecationResult:
    """
    Check if a given fides_key from the default taxonomy is deprecated, and if deprecated, provide the replacement details.

    Args:
        taxonomy_class: The taxonomy class to search (DataCategory, DataUse, or DataSubject)
        fides_key: The fides_key from the default taxonomy to check for deprecation

    Returns:
        CheckDeprecationResult: Object with deprecation check results including:
            - original_key: The input key that was checked
            - is_deprecated: Whether the key is deprecated and needs migration
            - replacement_key: The replacement key if deprecated (None otherwise)
            - fides_key: Property returning the key to use (replacement if deprecated, original if not)

    Raises:
        ValueError: If the fides_key is not found in the default taxonomy

    Example:
        >>> from fideslang.models import DataCategory
        >>> result = check_for_deprecated_default_fides_key(DataCategory, "user.biometric")
        >>> result.is_deprecated  # True (deprecated)
        >>> result.fides_key        # "user.biometrics" (replacement)

        >>> result = check_for_deprecated_default_fides_key(DataCategory, "user.contact.email")
        >>> result.is_deprecated  # False (not deprecated)
        >>> result.fides_key        # "user.contact.email" (same as original)

        >>> check_for_deprecated_default_fides_key(DataCategory, "user.nonexistent")
        # Raises ValueError
    """
    from fideslang.default_taxonomy import DEFAULT_TAXONOMY

    # Get the appropriate taxonomy collection based on the class
    if taxonomy_class == DataCategory:
        taxonomy_items = DEFAULT_TAXONOMY.data_category
    elif taxonomy_class == DataUse:
        taxonomy_items = DEFAULT_TAXONOMY.data_use
    elif taxonomy_class == DataSubject:
        taxonomy_items = DEFAULT_TAXONOMY.data_subject
    else:
        raise ValueError(f"Unsupported taxonomy class: {taxonomy_class}")

    # Find the item with the matching fides_key
    for item in taxonomy_items:
        if item.fides_key == fides_key:
            is_deprecated = bool(item.version_deprecated)
            return CheckDeprecationResult(
                original_key=fides_key,
                is_deprecated=is_deprecated,
                replacement_key=item.replaced_by if is_deprecated else None,
            )

    # Resource not found - raise error
    taxonomy_name = taxonomy_class.__name__.lower().replace("data", "data ")
    raise ValueError(f"'{fides_key}' not found in {taxonomy_name} taxonomy")
