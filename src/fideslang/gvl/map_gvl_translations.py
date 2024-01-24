from collections import defaultdict
from json import dump
from typing import Any, Optional

from requests import get

OFFICIAL_GVL_URL = "https://vendor-list.consensu.org/v3/vendor-list.json"


def get_translation_links() -> dict[str, str]:
    """
    Get all translation links. Returns a dict mapping the language ID to the translation URL.

    Eventually it would be nice to dynamically determine this via some (structured) hosted list/registry...
    For now, "handmade" by looking at https://register.consensu.org/Translation.
    """
    languages = [
        "ar",
        "bg",
        "bs",
        "ca",
        "cs",
        "da",
        "de",
        "el",
        "es",
        "et",
        "fi",
        "fr",
        "gl",
        "hr",
        "hu",
        "it",
        "ja",
        "lt",
        "lv",
        "mt",
        "nl",
        "no",
        "pl",
        "pt-br",
        "pt-pt",
        "ro",
        "sr-cyrl",
        "sr-latn",
        "ru",
        "sk",
        "sl",
        "sv",
        "tr",
        "uk",
        "zh",
    ]
    return {
        language: f"https://vendor-list.consensu.org/v3/purposes-{language}.json"
        for language in languages
    }


def get_gvl() -> dict[str, Any]:
    return get(OFFICIAL_GVL_URL).json()


TRANSLATION_FIELDS = ["name", "description", "illustrations"]
GVL_ELEMENT_TYPES = [
    "purposes",
    "specialPurposes",
    "features",
    "specialFeatures",
    "dataCategories",
]


def extract_translation_record(element_record: dict[str, Any]) -> dict[str, Any]:
    """
    Extracts a translation record from a top-level element record.
    Removes translation fields from the top-level element record by mutating the given element record dict.
    """

    return {
        translation_field: element_record.pop(translation_field)
        for translation_field in TRANSLATION_FIELDS
        if translation_field in element_record
    }


def populate_base_mappings(
    translation_language: str,
    translation_source: dict[str, Any],
    mappings: Optional[dict[str, dict]] = None,
) -> dict[str, dict]:
    """Populates our "base" mapping dictionaries for all data types with the "default" english translations provided by the GVL."""
    if mappings is None:
        mappings = defaultdict(dict)

    for gvl_element_type in GVL_ELEMENT_TYPES:
        elements = translation_source[gvl_element_type]

        if not mappings[gvl_element_type]:
            mappings[gvl_element_type] = defaultdict(dict)
        for id, element in elements.items():
            mappings[gvl_element_type][id][translation_language] = element
            for key, value in mappings[gvl_element_type][id][
                translation_language
            ].items():
                if isinstance(value, str):
                    mappings[gvl_element_type][id][translation_language][
                        key
                    ] = value.rstrip()
                elif isinstance(value, list):
                    newlist = []
                    for listval in value:
                        if isinstance(listval, str):
                            newlist.append(listval.rstrip())
                        else:
                            newlist.append(listval)
                    mappings[gvl_element_type][id][translation_language][key] = newlist

    return mappings


def main():
    translation_links = get_translation_links()
    gvl = get_gvl()
    mappings = populate_base_mappings("en", gvl)
    for translation_language, translation_link in translation_links.items():
        populate_base_mappings(
            translation_language, get(translation_link).json(), mappings=mappings
        )

    with open("translations.json", "w", encoding="utf8") as json_file:
        dump(
            mappings,
            json_file,
            ensure_ascii=False,
            indent=4,
        )


if __name__ == "__main__":
    main()
