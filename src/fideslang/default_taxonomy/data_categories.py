from fideslang.models import DataCategory

DEFAULT_DATA_CATEGORIES = [
    DataCategory(
        fides_key="user",
        organization_fides_key="default_organization",
        name="User Data",
        description="Data related to the user of the system, either provided directly or derived based on their usage.",
        parent_key=None,
        is_default=True,
    ),
    DataCategory(
        fides_key="user.payment",
        organization_fides_key="default_organization",
        name="Payment Data",
        description="Payment data related to user.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.payment.financial_account_number",
        organization_fides_key="default_organization",
        name="Account Payment Financial Account Number",
        description="Financial account number for an account's payment card, bank account, or other financial system.",
        parent_key="user.payment",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.biometric",
        organization_fides_key="default_organization",
        name="Biometric Data",
        description="Encoded characteristics provided by a user.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.biometric_health",
        organization_fides_key="default_organization",
        name="Biometric Health Data",
        description="Encoded characteristic collected about a user.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.browsing_history",
        organization_fides_key="default_organization",
        name="Browsing History",
        description="Content browsing history of a user.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.demographic",
        organization_fides_key="default_organization",
        name="Demographic Data",
        description="Demographic data about a user.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.contact",
        organization_fides_key="default_organization",
        name="Contact Data",
        description="Contact data collected about a user.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.contact.address",
        organization_fides_key="default_organization",
        name="Contact Data",
        description="Contact address data collected about a user.",
        parent_key="user.contact",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.device",
        organization_fides_key="default_organization",
        name="Device Data",
        description="Data related to a user's device, configuration and setting.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.device.cookie_id",
        organization_fides_key="default_organization",
        name="Cookie ID",
        description="Cookie unique identification number.",
        parent_key="user.device",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.device.device_id",
        organization_fides_key="default_organization",
        name="Device ID",
        description="Device unique identification number.",
        parent_key="user.device",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.device.ip_address",
        organization_fides_key="default_organization",
        name="IP Address",
        description="Unique identifier related to device connection.",
        parent_key="user.device",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.gender",
        organization_fides_key="default_organization",
        name="Gender",
        description="Gender of an individual.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.location",
        organization_fides_key="default_organization",
        name="Location Data",
        description="Records of the location of a user.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.media_consumption",
        organization_fides_key="default_organization",
        name="Media Consumption Data",
        description="Media type consumption data of a user.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.non_specific_age",
        organization_fides_key="default_organization",
        name="Non-Specific Age",
        description="Age range data.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.observed",
        organization_fides_key="default_organization",
        name="Observed Data",
        description="Data collected through observation of use of the system.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.profiling",
        organization_fides_key="default_organization",
        name="Profiling Data",
        description="Preference and interest data about a user.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.race",
        organization_fides_key="default_organization",
        name="Race",
        description="Racial or ethnic origin data.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.religious_belief",
        organization_fides_key="default_organization",
        name="Religious Belief",
        description="Religion or religious belief.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.search_history",
        organization_fides_key="default_organization",
        name="Search History",
        description="Records of search history and queries of a user.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.sexual_orientation",
        organization_fides_key="default_organization",
        name="Sexual Orientation",
        description="Personal sex life or sexual data.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.social",
        organization_fides_key="default_organization",
        name="Social Data",
        description="Social activity and interaction data.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.telemetry",
        organization_fides_key="default_organization",
        name="Telemetry Data",
        description="User identifiable measurement data from system sensors and monitoring.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.unique_id",
        organization_fides_key="default_organization",
        name="Unique ID",
        description="Unique identifier for a user assigned through system use.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.user_sensor",
        organization_fides_key="default_organization",
        name="User Sensor Data",
        description="Measurement data about a user's environment through system use.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.organization",
        organization_fides_key="default_organization",
        name="Organization Identifiable Data",
        description="Data that is linked to, or identifies an organization.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.workplace",
        organization_fides_key="default_organization",
        name="Workplace",
        description="Organization of employment.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.sensor",
        organization_fides_key="default_organization",
        name="Sensor Data",
        description="Measurement data from sensors and monitoring systems.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.childrens",
        organization_fides_key="default_organization",
        name="Children's Data",
        description="Data relating to children.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.contact.address.city",
        organization_fides_key="default_organization",
        name="User Contact City",
        description="User's city level address data.",
        parent_key="user.contact.address",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.contact.address.country",
        organization_fides_key="default_organization",
        name="User Contact Country",
        description="User's country level address data.",
        parent_key="user.contact.address",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.contact.email",
        organization_fides_key="default_organization",
        name="User Contact Email",
        description="User's contact email address.",
        parent_key="user.contact",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.contact.phone_number",
        organization_fides_key="default_organization",
        name="User Contact Phone Number",
        description="User's phone number.",
        parent_key="user.contact",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.contact.address.postal_code",
        organization_fides_key="default_organization",
        name="User Contact Postal Code",
        description="User's postal code.",
        parent_key="user.contact.address",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.contact.address.state",
        organization_fides_key="default_organization",
        name="User Contact State",
        description="User's state level address data.",
        parent_key="user.contact.address",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.contact.address.street",
        organization_fides_key="default_organization",
        name="User Contact Street",
        description="User's street level address data.",
        parent_key="user.contact.address",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.credentials",
        organization_fides_key="default_organization",
        name="Credentials",
        description="User authentication data.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.credentials.biometric_credentials",
        organization_fides_key="default_organization",
        name="Biometric Credentials",
        description="Credentials for system authentication.",
        parent_key="user.credentials",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.credentials.password",
        organization_fides_key="default_organization",
        name="Password",
        description="Password for system authentication.",
        parent_key="user.credentials",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.date_of_birth",
        organization_fides_key="default_organization",
        name="Date of Birth",
        description="User's date of birth.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.financial",
        organization_fides_key="default_organization",
        name="Financial Data",
        description="Payment data and financial history.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.financial.account_number",
        organization_fides_key="default_organization",
        name="User Financial Account Number",
        description="User's account number for a payment card, bank account, or other financial system.",
        parent_key="user.financial",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.genetic",
        organization_fides_key="default_organization",
        name="Genetic Data",
        description="Data about the genetic makeup provided by a user.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.government_id",
        organization_fides_key="default_organization",
        name="Government ID",
        description="State provided identification data.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.government_id.drivers_license_number",
        organization_fides_key="default_organization",
        name="Driver's License Number",
        description="State issued driving identification number.",
        parent_key="user.government_id",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.government_id.national_identification_number",
        organization_fides_key="default_organization",
        name="National Identification Number",
        description="State issued personal identification number.",
        parent_key="user.government_id",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.government_id.passport_number",
        organization_fides_key="default_organization",
        name="Passport Number",
        description="State issued passport data.",
        parent_key="user.government_id",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.health_and_medical",
        organization_fides_key="default_organization",
        name="Health and Medical Data",
        description="Health records or individual's personal medical information.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.job_title",
        organization_fides_key="default_organization",
        name="Job Title",
        description="Professional data.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.name",
        organization_fides_key="default_organization",
        name="Name",
        description="User's real name.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="user.political_opinion",
        organization_fides_key="default_organization",
        name="Political Opinion",
        description="Data related to the individual's political opinions.",
        parent_key="user",
        is_default=True,
    ),
    DataCategory(
        fides_key="system",
        organization_fides_key="default_organization",
        name="System Data",
        description="Data unique to, and under control of the system.",
        parent_key=None,
        is_default=True,
    ),
    DataCategory(
        fides_key="system.authentication",
        organization_fides_key="default_organization",
        name="Authentication Data",
        description="Data used to manage access to the system.",
        parent_key="system",
        is_default=True,
    ),
    DataCategory(
        fides_key="system.operations",
        organization_fides_key="default_organization",
        name="Operations Data",
        description="Data used for system operations.",
        parent_key="system",
        is_default=True,
    ),
]