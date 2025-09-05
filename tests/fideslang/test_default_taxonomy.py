from collections import Counter
from typing import Tuple

import pytest

from fideslang.default_taxonomy import DEFAULT_TAXONOMY

# Updated counts for v3.2.0 - includes both active and deprecated categories
taxonomy_counts = {
    "data_category": 123,  # Updated for v3.2.0 (38 new + existing + deprecated)
    "data_use": 56,
    "data_subject": 15,
}

# Active (non-deprecated) category counts for v3.2.0
active_taxonomy_counts = {
    "data_category": 101,  # Only non-deprecated categories
    "data_use": 56,
    "data_subject": 15,
}


class TestDefaultTaxonomy:
    @pytest.mark.parametrize(
        "type_and_count", taxonomy_counts.items(), ids=lambda items: items[0]
    )
    def test_taxonomy_count(self, type_and_count: Tuple[str, int]) -> None:
        data_type = type_and_count[0]
        expected_count = type_and_count[1]
        assert len(getattr(DEFAULT_TAXONOMY, data_type)) == expected_count

    @pytest.mark.parametrize("data_type", taxonomy_counts.keys())
    def test_are_set_as_default(self, data_type: str) -> None:
        assert all([x.is_default for x in getattr(DEFAULT_TAXONOMY, data_type)])

    @pytest.mark.parametrize("data_type", taxonomy_counts.keys())
    def test_key_uniqueness(self, data_type: str) -> None:
        keys = [x.fides_key for x in getattr(DEFAULT_TAXONOMY, data_type)]
        duplicate_keys = {
            key: value for key, value in Counter(keys).items() if value > 1
        }
        print(duplicate_keys)
        assert not duplicate_keys

    @pytest.mark.parametrize("data_type", taxonomy_counts.keys())
    def test_name_uniqueness_active_only(self, data_type: str) -> None:
        """Test name uniqueness for active (non-deprecated) categories only."""
        # Only check active categories to avoid migration-period duplicate names
        items = getattr(DEFAULT_TAXONOMY, data_type)
        active_items = [x for x in items if not x.version_deprecated]
        names = [x.name for x in active_items]
        duplicate_names = {
            name: count for name, count in Counter(names).items() if count > 1
        }
        print(f"Duplicate names in active {data_type}:", duplicate_names)
        assert not duplicate_names, f"Found duplicate names in active {data_type}: {duplicate_names}"

    @pytest.mark.parametrize("data_type", ["data_category"])
    def test_migration_name_duplicates_expected(self, data_type: str) -> None:
        """Test that migration creates expected name duplicates between old and new versions."""
        items = getattr(DEFAULT_TAXONOMY, data_type)
        all_names = [x.name for x in items]
        duplicate_names = {
            name: count for name, count in Counter(all_names).items() if count > 1
        }
        
        # During v3.2.0 migration, we expect some duplicates
        if data_type == "data_category":
            # These are expected duplicates during migration
            expected_duplicates = {
                "Biometric Credentials", "Fingerprint", "Retina Scan", "Voice Recording",
                "User's Genetic Data", "Medical Insurance ID", "Medical Record ID",
                "Workplace", "Children's Data", "Biometric Data", "Job Title"
            }
            actual_duplicates = set(duplicate_names.keys())
            
            # All duplicates should be expected migration duplicates
            unexpected = actual_duplicates - expected_duplicates
            assert not unexpected, f"Unexpected duplicate names (not part of planned migration): {unexpected}"

    @pytest.mark.parametrize("data_type", taxonomy_counts.keys())
    def test_description_uniqueness(self, data_type: str) -> None:
        keys = [
            x.description
            for x in getattr(DEFAULT_TAXONOMY, data_type)
            if not x.version_deprecated
        ]
        duplicate_keys = {
            key: value for key, value in Counter(keys).items() if value > 1
        }
        print(duplicate_keys)
        assert not duplicate_keys

    @pytest.mark.parametrize("data_type", ["data_category", "data_use"])
    def test_parent_keys_exist(self, data_type: str) -> None:
        """This test catches any keys that are used as parents but don't exist as fides keys."""
        fides_keys = set([x.fides_key for x in getattr(DEFAULT_TAXONOMY, data_type)])
        parent_keys = set(
            [x.parent_key for x in getattr(DEFAULT_TAXONOMY, data_type) if x.parent_key]
        )
        diff = parent_keys.difference(fides_keys)
        assert not diff


class TestTaxonomyMigrationV32:
    """Tests specific to v3.2.0 taxonomy migration."""

    def test_v32_new_categories_exist(self) -> None:
        """Test that all expected new v3.2.0 categories exist."""
        expected_new_categories = {
            "user.biometrics",
            "user.children", 
            "user.children.children_under_thirteen",
            "user.children.thirteen_to_sixteen",
            "user.health",
            "user.health.baby_formula",
            "user.health.condition",
            "user.health.medical_diagnosis", 
            "user.health.medications",
            "user.health.prescriptions",
            "user.health.reproductive_or_sexual",
            "user.health.social_psychological_behavioral",
            "user.health.symptons",
            "user.health.treatment",
            "user.health.maternity_clothing",
            "user.professional_information",
            "user.professional_information.job_title",
            "user.professional_information.workplace", 
            "user.settings",
            "user.social_activity",
            "user.authorization.biometrics",
            "user.biometrics.fingerprint",
            "user.biometrics.retinal",
            "user.biometrics.voice",
            "user.contact.social_url",
            "user.contact.address.mailing_address",
            "user.demographic.citizenship_or_immigration_status",
            "user.demographic.philosophical_belief",
            "user.demographic.protected_classifications",
            "user.demographic.union_membership",
            "user.device.sensor",
            "user.device.telemetry",
            "user.health.genetic",
            "user.health.insurance_beneficiary_id",
            "user.health.record_id",
            "user.location.coarse",
            "user.unique_id.deterministic",
            "user.unique_id.probablistic",
        }
        
        actual_keys = {cat.fides_key for cat in DEFAULT_TAXONOMY.data_category}
        missing_categories = expected_new_categories - actual_keys
        assert not missing_categories, f"Missing expected v3.2.0 categories: {missing_categories}"
        
        # Verify they all have version_added = "3.2.0"
        v32_categories = {
            cat.fides_key: cat for cat in DEFAULT_TAXONOMY.data_category 
            if cat.fides_key in expected_new_categories
        }
        
        incorrect_versions = {
            key: cat.version_added for key, cat in v32_categories.items() 
            if cat.version_added != "3.2.0"
        }
        assert not incorrect_versions, f"Categories with incorrect version_added: {incorrect_versions}"

    def test_v32_deprecated_categories_have_replacements(self) -> None:
        """Test that all deprecated v3.2.0 categories have proper replaced_by pointers."""
        expected_replacements = {
            "user.biometric": "user.biometrics",
            "user.biometric.fingerprint": "user.biometrics.fingerprint",
            "user.biometric.retinal": "user.biometrics.retinal", 
            "user.biometric.voice": "user.biometrics.voice",
            "user.childrens": "user.children",
            "user.contact.url": "user.contact.social_url",
            "user.health_and_medical": "user.health",
            "user.health_and_medical.genetic": "user.health.genetic",
            "user.health_and_medical.insurance_beneficiary_id": "user.health.insurance_beneficiary_id",
            "user.health_and_medical.record_id": "user.health.record_id",
            "user.location.imprecise": "user.location.coarse",
            "user.job_title": "user.professional_information.job_title",
            "user.workplace": "user.professional_information.workplace",
            "user.account.settings": "user.settings",
            "user.social": "user.social_activity",
            "user.authorization.biometric": "user.authorization.biometrics",
            "user.sensor": "user.device.sensor",
            "user.telemetry": "user.device.telemetry",
            # Merged categories
            "user.biometric.health": "user.biometrics",
            "user.contact.organization": "user.contact",
            "user.user_sensor": "user.device.sensor",
            "user.unique_id.pseudonymous": "user.unique_id",
        }
        
        category_map = {cat.fides_key: cat for cat in DEFAULT_TAXONOMY.data_category}
        
        for old_key, expected_replacement in expected_replacements.items():
            assert old_key in category_map, f"Expected deprecated category {old_key} not found"
            cat = category_map[old_key]
            assert cat.version_deprecated == "3.2.0", f"Category {old_key} should be deprecated in v3.2.0"
            assert cat.replaced_by == expected_replacement, f"Category {old_key} should be replaced by {expected_replacement}, got {cat.replaced_by}"

    def test_v32_merged_categories(self) -> None:
        """Test that merged categories point to their parent categories."""
        merged_categories = {
            "user.biometric.health": "user.biometrics",
            "user.contact.organization": "user.contact", 
            "user.user_sensor": "user.device.sensor",
            "user.unique_id.pseudonymous": "user.unique_id",
        }
        
        category_map = {cat.fides_key: cat for cat in DEFAULT_TAXONOMY.data_category}
        
        for merged_key, target_key in merged_categories.items():
            merged_cat = category_map[merged_key]
            assert merged_cat.version_deprecated == "3.2.0"
            assert merged_cat.replaced_by == target_key
            
            # Ensure target category exists
            assert target_key in category_map, f"Merge target {target_key} does not exist"

    def test_active_category_count(self) -> None:
        """Test that we have the expected number of active (non-deprecated) categories."""
        active_categories = [
            cat for cat in DEFAULT_TAXONOMY.data_category 
            if not cat.version_deprecated
        ]
        expected_active_count = active_taxonomy_counts["data_category"]
        actual_count = len(active_categories)
        assert actual_count == expected_active_count, f"Expected {expected_active_count} active categories, got {actual_count}"


