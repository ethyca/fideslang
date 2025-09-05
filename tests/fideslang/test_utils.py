import pytest

from fideslang.default_taxonomy import check_for_deprecated_default_fides_key, CheckDeprecationResult
from fideslang.models import DataCategory, DataSubject, DataUse
from fideslang.utils import get_resource_by_fides_key


@pytest.mark.unit
class TestCheckForDeprecatedDefaultFidesKey:
    """Test the deprecated default fides_key checking function."""

    def test_deprecated_category_returns_replacement(self):
        """Test that deprecated categories are identified and return their replacement keys."""
        # Test a few known deprecated categories from v3.2.0
        result = check_for_deprecated_default_fides_key(DataCategory, "user.biometric")
        assert result.is_deprecated is True
        assert result.replacement_key == "user.biometrics"
        assert result.fides_key == "user.biometrics"
        
        result = check_for_deprecated_default_fides_key(DataCategory, "user.childrens")
        assert result.is_deprecated is True
        assert result.fides_key == "user.children"
        
        result = check_for_deprecated_default_fides_key(DataCategory, "user.health_and_medical")
        assert result.is_deprecated is True
        assert result.fides_key == "user.health"

    def test_active_category_not_deprecated(self):
        """Test that active (non-deprecated) categories are identified as not deprecated."""
        # Test some known active categories
        result = check_for_deprecated_default_fides_key(DataCategory, "user.contact.email")
        assert result.is_deprecated is False
        assert result.replacement_key is None
        assert result.fides_key == "user.contact.email"
        
        result = check_for_deprecated_default_fides_key(DataCategory, "user.biometrics")  # New category
        assert result.is_deprecated is False
        assert result.fides_key == "user.biometrics"

    def test_nonexistent_key_raises_error(self):
        """Test that non-existent default taxonomy fides_keys raise ValueError."""
        with pytest.raises(ValueError, match="'user.nonexistent' not found in data category taxonomy"):
            check_for_deprecated_default_fides_key(DataCategory, "user.nonexistent")
        
        with pytest.raises(ValueError, match="'' not found in data category taxonomy"):
            check_for_deprecated_default_fides_key(DataCategory, "")

    def test_merged_categories_return_replacement(self):
        """Test that merged categories are identified as deprecated and return their replacement keys."""
        # Test some known merged categories from v3.2.0
        result = check_for_deprecated_default_fides_key(DataCategory, "user.biometric.health")
        assert result.is_deprecated is True
        assert result.fides_key == "user.biometrics"
        
        result = check_for_deprecated_default_fides_key(DataCategory, "user.contact.organization")
        assert result.is_deprecated is True
        assert result.fides_key == "user.contact"

    def test_works_with_data_uses(self):
        """Test that the function works with data uses to check for deprecation."""
        # Test with active data uses
        result = check_for_deprecated_default_fides_key(DataUse, "analytics.reporting")
        assert result.is_deprecated is False
        assert result.fides_key == "analytics.reporting"

    def test_works_with_data_subjects(self):
        """Test that the function works with data subjects to check for deprecation."""
        # Test with active data subjects
        result = check_for_deprecated_default_fides_key(DataSubject, "customer")
        assert result.is_deprecated is False
        assert result.fides_key == "customer"

    def test_replacement_chain_follows_to_end(self):
        """Test that if there are chained replacements, it returns the immediate replacement."""
        # The function should return the direct replacement, not follow the entire chain
        # If user.biometric -> user.biometrics, it should return "user.biometrics"
        # even if user.biometrics were to be deprecated later
        result = check_for_deprecated_default_fides_key(DataCategory, "user.biometric")
        assert result.fides_key == "user.biometrics"
        
        # The replacement itself should not be deprecated (in our current taxonomy)
        replacement_result = check_for_deprecated_default_fides_key(DataCategory, result.fides_key)
        assert replacement_result.is_deprecated is False  # user.biometrics is not deprecated
        
    def test_invalid_taxonomy_class_raises_error(self):
        """Test that invalid taxonomy classes raise ValueError."""
        with pytest.raises(ValueError, match="Unsupported taxonomy class"):
            check_for_deprecated_default_fides_key(str, "some.key")  # Invalid class

    def test_migration_result_properties(self):
        """Test that CheckDeprecationResult properties work correctly."""
        # Test deprecated key
        result = check_for_deprecated_default_fides_key(DataCategory, "user.biometric")
        assert isinstance(result, CheckDeprecationResult)
        assert result.original_key == "user.biometric"
        assert result.is_deprecated is True
        assert result.replacement_key == "user.biometrics"
        assert result.fides_key == "user.biometrics"
        
        # Test active key
        result = check_for_deprecated_default_fides_key(DataCategory, "user.contact.email")
        assert result.original_key == "user.contact.email"
        assert result.is_deprecated is False
        assert result.replacement_key is None
        assert result.fides_key == "user.contact.email"