from fideslang.models import DataUse

DEFAULT_DATA_USES = [
    DataUse(
        fides_key="provide",
        organization_fides_key="default_organization",
        name="Provide the capability",
        description="Provide, give, or make available the product, service, application or system.",
        parent_key=None,
        is_default=True,
    ),
    DataUse(
        fides_key="provide.service",
        organization_fides_key="default_organization",
        name="Service",
        description="The source service, system, or product being provided to the user.",
        parent_key="provide",
        is_default=True,
    ),
    DataUse(
        fides_key="provide.service.operations",
        organization_fides_key="default_organization",
        name="Service Operations",
        description="Use of specified data categories to operate and protect in order to provide the service.",
        parent_key="provide.service",
        is_default=True,
    ),
    DataUse(
        fides_key="provide.service.operations.support",
        organization_fides_key="default_organization",
        name="Operations Support",
        description="Use of specified data categories to provide support for operation and protection in order to provide the service.",
        parent_key="provide.service.operations",
        is_default=True,
    ),
    DataUse(
        fides_key="provide.service.operations.support.optimization",
        organization_fides_key="default_organization",
        name="Support Optimization",
        description="Use of specified data categories to optimize and improve support operations in order to provide the service.",
        parent_key="provide.service.operations.support",
        is_default=True,
    ),
    DataUse(
        fides_key="provide.service.upgrades",
        organization_fides_key="default_organization",
        name="Offer Upgrades",
        description="Offer upgrades or upsales such as increased capacity for the service based on monitoring of service usage.",
        parent_key="provide.service",
        is_default=True,
    ),
    DataUse(
        fides_key="improve",
        organization_fides_key="default_organization",
        name="Improve the capability",
        description="Improve the product, service, application or system.",
        parent_key=None,
        is_default=True,
    ),
    DataUse(
        fides_key="improve.system",
        organization_fides_key="default_organization",
        name="System",
        description="The source system, product, service or application being improved.",
        parent_key="improve",
        is_default=True,
    ),
    DataUse(
        fides_key="personalize",
        organization_fides_key="default_organization",
        name="Personalize the capability",
        description="Personalize the product, service, application or system.",
        parent_key=None,
        is_default=True,
    ),
    DataUse(
        fides_key="personalize.system",
        organization_fides_key="default_organization",
        name="System",
        description="The source system, product, service or application being personalized.",
        parent_key="personalize",
        is_default=True,
    ),
    DataUse(
        fides_key="advertising",
        organization_fides_key="default_organization",
        name="Advertising, Marketing or Promotion",
        description="The promotion of products or services targeted to users based on the the processing of user provided data in the system.",
        parent_key=None,
        is_default=True,
    ),
    DataUse(
        fides_key="advertising.first_party",
        organization_fides_key="default_organization",
        name="First Party Advertising",
        description="The promotion of products or services targeting users based on processing of derviced data from prior use of the system.",
        parent_key="advertising",
        is_default=True,
    ),
    DataUse(
        fides_key="advertising.third_party",
        organization_fides_key="default_organization",
        name="Third Party Advertising",
        description="The promotion of products or services targeting users based on processing of specific categories of data acquired from third party sources.",
        parent_key="advertising",
        is_default=True,
    ),
    DataUse(
        fides_key="advertising.first_party.contextual",
        organization_fides_key="default_organization",
        name="First Party Contextual Advertising",
        description="The promotion of products or services targeted to users based on the processing of data from the users prior use of the services.",
        parent_key="advertising.first_party",
        is_default=True,
    ),
    DataUse(
        fides_key="advertising.first_party.personalized",
        organization_fides_key="default_organization",
        name="First Party Personalized Advertising",
        description="The targeting and changing of promotional content based on processing of specific data categories from the user.",
        parent_key="advertising.first_party",
        is_default=True,
    ),
    DataUse(
        fides_key="advertising.third_party.personalized",
        organization_fides_key="default_organization",
        name="Third Party Personalized Advertising",
        description="The targeting and changing of promotional content based on processing of specific categories of user data acquired from third party sources.",
        parent_key="advertising.third_party",
        is_default=True,
    ),
    DataUse(
        fides_key="third_party_sharing",
        organization_fides_key="default_organization",
        name="Third Party Sharing",
        description="The transfer of specified data categories to third parties outside of the system/application's scope.",
        parent_key=None,
        is_default=True,
    ),
    DataUse(
        fides_key="third_party_sharing.payment_processing",
        organization_fides_key="default_organization",
        name="Sharing for Processing Payments",
        description="Sharing of specified data categories with a third party for payment processing.",
        parent_key="third_party_sharing",
        is_default=True,
    ),
    DataUse(
        fides_key="third_party_sharing.personalized_advertising",
        organization_fides_key="default_organization",
        name="Sharing for Personalized Advertising",
        description="Sharing of specified data categories for the purpose of marketing/advertising/promotion.",
        parent_key="third_party_sharing",
        is_default=True,
    ),
    DataUse(
        fides_key="third_party_sharing.fraud_detection",
        organization_fides_key="default_organization",
        name="Sharing for Fraud Detection",
        description="Sharing of specified data categories with a third party fo fraud prevention/detection.",
        parent_key="third_party_sharing",
        is_default=True,
    ),
    DataUse(
        fides_key="third_party_sharing.legal_obligation",
        organization_fides_key="default_organization",
        name="Sharing for Legal Obligation",
        description="Sharing of data for legal obligations, including contracts, applicable laws or regulations.",
        parent_key="third_party_sharing",
        is_default=True,
    ),
    DataUse(
        fides_key="collect",
        organization_fides_key="default_organization",
        name="Collect",
        description="Collecting and storing data in order to use it for another purpose such as data training for ML.",
        parent_key=None,
        is_default=True,
    ),
    DataUse(
        fides_key="train_ai_system",
        organization_fides_key="default_organization",
        name="Train AI System",
        description="Training an AI system. Please note when this data use is specified, the method and degree to which a user may be directly identified in the resulting AI system should be appended.",
        parent_key=None,
        is_default=True,
    ),
]