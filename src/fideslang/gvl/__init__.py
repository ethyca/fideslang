# pylint: disable=too-many-locals

import os
from collections import defaultdict
from json import load
from os.path import dirname, join
from typing import Dict, List, Optional

from .models import Feature, GVLDataCategory, MappedDataCategory, MappedPurpose, Purpose

DEFAULT_LANGUAGE_ID = "en"


### (Special) Purposes

PURPOSE_MAPPING_FILE = join(
    dirname(__file__),
    "",
    "gvl_data_use_mapping.json",
)

GVL_PURPOSES: Dict[int, Dict[str, Purpose]] = defaultdict(dict)
MAPPED_PURPOSES: Dict[int, Dict[str, MappedPurpose]] = defaultdict(dict)
GVL_SPECIAL_PURPOSES: Dict[int, Dict[str, Purpose]] = defaultdict(dict)
MAPPED_SPECIAL_PURPOSES: Dict[int, Dict[str, MappedPurpose]] = defaultdict(dict)
MAPPED_PURPOSES_BY_DATA_USE: Dict[str, Dict[str, MappedPurpose]] = defaultdict(dict)

### (Special) Features

FEATURE_MAPPING_FILE = join(
    dirname(__file__),
    "",
    "gvl_feature_mapping.json",
)
GVL_FEATURES: Dict[int, Dict[str, Feature]] = defaultdict(dict)
GVL_SPECIAL_FEATURES: Dict[int, Dict[str, Feature]] = defaultdict(dict)
FEATURES_BY_NAME: Dict[str, Feature] = {}


### Data Categories

DATA_CATEGORY_MAPPING_FILE = join(
    dirname(__file__),
    "",
    "gvl_data_category_mapping.json",
)
GVL_DATA_CATEGORIES: Dict[int, Dict[str, GVLDataCategory]] = defaultdict(dict)
MAPPED_GVL_DATA_CATEGORIES: Dict[int, Dict[str, MappedDataCategory]] = defaultdict(dict)


### Translations

TRANSLATIONS_FILE = join(
    dirname(__file__),
    "",
    "translations.json",
)


def _load_data() -> None:
    purpose_to_data_uses = {}
    special_purpose_to_data_uses = {}
    with open(
        os.path.join(os.curdir, PURPOSE_MAPPING_FILE), encoding="utf-8"
    ) as mapping_file:
        data = load(mapping_file)
        # first load purpose -> data use map based on purpose mapping file
        for raw_purpose in data["purposes"].values():
            purpose = MappedPurpose.parse_obj(raw_purpose)
            purpose_to_data_uses[purpose.id] = purpose.data_uses

        for raw_special_purpose in data["specialPurposes"].values():
            special_purpose = MappedPurpose.parse_obj(raw_special_purpose)
            special_purpose_to_data_uses[special_purpose.id] = special_purpose.data_uses

    gvl_category_to_fides_categories = {}
    with open(
        os.path.join(os.curdir, DATA_CATEGORY_MAPPING_FILE), encoding="utf-8"
    ) as mapping_file:
        data = load(mapping_file)
        # first load gvl category -> fides category map based on category mapping file
        for raw_data_category in data.values():
            data_category = MappedDataCategory.parse_obj(raw_data_category)
            gvl_category_to_fides_categories[
                data_category.id
            ] = data_category.fides_data_categories

    with open(
        os.path.join(os.curdir, TRANSLATIONS_FILE), encoding="utf-8"
    ) as translations_file:
        data = load(translations_file)
        for translation_dict in data["purposes"].values():
            for language, translation in translation_dict.items():
                purpose = Purpose.parse_obj(translation)
                mapped_purpose = MappedPurpose.parse_obj(
                    {
                        **translation,
                        "data_uses": purpose_to_data_uses[purpose.id],
                    }
                )
                GVL_PURPOSES[purpose.id][language] = purpose
                MAPPED_PURPOSES[mapped_purpose.id][language] = mapped_purpose
                for data_use in mapped_purpose.data_uses:
                    MAPPED_PURPOSES_BY_DATA_USE[data_use][language] = mapped_purpose

        for translation_dict in data["specialPurposes"].values():
            for language, translation in translation_dict.items():
                purpose = Purpose.parse_obj(translation)
                mapped_purpose = MappedPurpose.parse_obj(
                    {
                        **translation,
                        "data_uses": special_purpose_to_data_uses[purpose.id],
                    }
                )
                GVL_SPECIAL_PURPOSES[purpose.id][language] = purpose
                MAPPED_SPECIAL_PURPOSES[mapped_purpose.id][language] = mapped_purpose
                for data_use in mapped_purpose.data_uses:
                    MAPPED_PURPOSES_BY_DATA_USE[data_use][language] = mapped_purpose

        for translation_dict in data["features"].values():
            for language, translation in translation_dict.items():
                feature = Feature.parse_obj(translation)
                GVL_FEATURES[feature.id][language] = feature
                if language == DEFAULT_LANGUAGE_ID:
                    FEATURES_BY_NAME[feature.name] = feature

        for translation_dict in data["specialFeatures"].values():
            for language, translation in translation_dict.items():
                special_feature = Feature.parse_obj(translation)
                GVL_SPECIAL_FEATURES[special_feature.id][language] = special_feature
                if language == DEFAULT_LANGUAGE_ID:
                    FEATURES_BY_NAME[special_feature.name] = special_feature

        for translation_dict in data["dataCategories"].values():
            for language, translation in translation_dict.items():
                category = GVLDataCategory.parse_obj(translation)
                mapped_category = MappedDataCategory.parse_obj(
                    {
                        **translation,
                        "fides_data_categories": gvl_category_to_fides_categories[
                            category.id
                        ],
                    }
                )

                GVL_DATA_CATEGORIES[category.id][language] = category
                MAPPED_GVL_DATA_CATEGORIES[category.id][language] = mapped_category


def purpose_to_data_use(purpose_id: int, special_purpose: bool = False) -> List[str]:
    """
    Utility function to return the fideslang data uses associated with the
    given GVL purpose (or special purpose) ID.

    By default, the given ID is treated as a purpose ID. The `special_purpose`
    argument can be set to `True` if looking up special purpose IDs.

    Raises a KeyError if an invalid purpose ID is provided.
    """
    purpose_map = MAPPED_SPECIAL_PURPOSES if special_purpose else MAPPED_PURPOSES
    return purpose_map[purpose_id][DEFAULT_LANGUAGE_ID].data_uses


def data_use_to_purpose(
    data_use: str,
    language: str = DEFAULT_LANGUAGE_ID,
) -> Optional[Purpose]:
    """
    Utility function to return the GVL purpose (or special purpose) associated
    with the given fideslang data use.

    Returns None if no associated purpose (or special purpose) is found
    """
    return MAPPED_PURPOSES_BY_DATA_USE.get(data_use, {}).get(language, None)


def feature_name_to_feature(feature_name: str) -> Optional[Feature]:
    """Utility function to return a GVL feature (or special feature) given the feature's name"""
    return FEATURES_BY_NAME.get(feature_name, None)


def feature_id_to_feature_name(
    feature_id: int,
    language: str = DEFAULT_LANGUAGE_ID,
    special_feature: bool = False,
) -> Optional[str]:
    """Utility function to return a GVL feature/special feature name given the feature/special feature's id"""
    feature_map = GVL_SPECIAL_FEATURES if special_feature else GVL_FEATURES
    feature = feature_map.get(feature_id, {}).get(language, None)
    if not feature:
        return None
    return feature.name


def data_category_id_to_data_categories(data_category_id: int) -> List[str]:
    """
    Utility function to return the fideslang data categories associated with the
    given GVL data category ID.

    Raises a KeyError if an invalid GVL data category ID is provided.
    """
    return MAPPED_GVL_DATA_CATEGORIES[data_category_id][
        DEFAULT_LANGUAGE_ID
    ].fides_data_categories


_load_data()
