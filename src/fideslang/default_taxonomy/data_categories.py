from functools import partial

from fideslang.models import DataCategory

from .utils import default_factory

default_category_factory = partial(default_factory, taxonomy_class=DataCategory)

DEFAULT_DATA_CATEGORIES = [
    # user
    default_category_factory(
        fides_key="user",
        name="User Data",
        description="Data related to the user of the system, either provided directly or derived based on their usage.",
    ),
    # user.account
    default_category_factory(
        fides_key="user.account",
        name="Account Information",
        description="Account creation or registration information.",
        parent_key="user",
    ),
    default_category_factory(
        fides_key="user.account.settings",
        name="Account Settings",
        description="Account preferences and settings.",
        parent_key="user.account",
        version_deprecated="3.2.0",
        replaced_by="user.settings",
    ),
    default_category_factory(
        fides_key="user.account.username",
        name="Account Username",
        description="Username associated with account.",
        parent_key="user.account",
    ),
    ######################
    # user.authorization #
    ######################
    default_category_factory(
        fides_key="user.authorization",
        name="Authorization Information",
        description="Scope of permissions and access to a system.",
        parent_key="user",
    ),
    default_category_factory(
        fides_key="user.authorization.credentials",
        name="Account password",
        description="Authentication credentials to a system.",
        parent_key="user.authorization",
    ),
    default_category_factory(
        fides_key="user.authorization.biometric",
        name="Biometric Credentials",
        description="Credentials for system authentication.",
        parent_key="user.authorization",
        version_deprecated="3.2.0",
        replaced_by="user.authorization.biometrics",
    ),
    default_category_factory(
        fides_key="user.authorization.biometrics",
        name="Biometric Authentication",
        description="Credentials for system authentication.",
        parent_key="user.authorization",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.authorization.password",
        name="Password",
        description="Password for system authentication.",
        parent_key="user.authorization",
    ),
    #################
    # user.behavior #
    #################
    default_category_factory(
        fides_key="user.behavior",
        name="Observed Behavior",
        description="Behavioral data about the subject.",
        parent_key="user",
    ),
    default_category_factory(
        fides_key="user.behavior.browsing_history",
        name="Browsing History",
        description="Content browsing history of a user.",
        parent_key="user.behavior",
    ),
    default_category_factory(
        fides_key="user.behavior.media_consumption",
        name="Media Consumption",
        description="Content consumption history of the subject.",
        parent_key="user.behavior",
    ),
    default_category_factory(
        fides_key="user.behavior.purchase_history",
        name="Purchase History",
        description="Purchase history of the subject.",
        parent_key="user.behavior",
    ),
    default_category_factory(
        fides_key="user.behavior.search_history",
        name="Search History",
        description="Search history of the subject.",
        parent_key="user.behavior",
    ),
    ##################
    # user.biometric #
    ##################
    default_category_factory(
        fides_key="user.biometric",
        name="Biometric Data",
        description="Encoded characteristics provided by a user.",
        parent_key="user",
        version_deprecated="3.2.0",
        replaced_by="user.biometrics",
    ),
    default_category_factory(
        fides_key="user.biometrics",
        name="Biometrics",
        description="Encoded characteristics provided by a user.",
        parent_key="user",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.biometric.fingerprint",
        name="Fingerprint",
        description="Fingerprint encoded data about a subject.",
        parent_key="user.biometric",
        version_deprecated="3.2.0",
        replaced_by="user.biometrics.fingerprint",
    ),
    default_category_factory(
        fides_key="user.biometrics.fingerprint",
        name="Fingerprint Data",
        description="Fingerprint encoded data about a subject.",
        parent_key="user.biometrics",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.biometric.retinal",
        name="Retina Scan",
        description="Retinal data about a subject.",
        parent_key="user.biometric",
        version_deprecated="3.2.0",
        replaced_by="user.biometrics.retinal",
    ),
    default_category_factory(
        fides_key="user.biometrics.retinal",
        name="Retinal Data",
        description="Retinal data about a subject.",
        parent_key="user.biometrics",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.biometric.voice",
        name="Voice Recording",
        description="Voice encoded data about a subject.",
        parent_key="user.biometric",
        version_deprecated="3.2.0",
        replaced_by="user.biometrics.voice",
    ),
    default_category_factory(
        fides_key="user.biometrics.voice",
        name="Voice Data",
        description="Voice encoded data about a subject.",
        parent_key="user.biometrics",
        version_added="3.2.0",
    ),
    # MERGED: user.biometric.health merged into user.biometrics
    default_category_factory(
        fides_key="user.biometric.health",
        name="Biometric Health Data",
        description="Encoded characteristic collected about a user.",
        parent_key="user.biometric",
        version_deprecated="3.2.0",
        replaced_by="user.biometrics",
    ),
    ##################
    # user.childrens #
    ##################
    default_category_factory(
        fides_key="user.childrens",
        name="Children's Data",
        description="Data relating to children.",
        parent_key="user",
        version_deprecated="3.2.0",
        replaced_by="user.children",
    ),
    default_category_factory(
        fides_key="user.children",
        name="Children",
        description="Data relating to children.",
        parent_key="user",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.children.children_under_thirteen",
        name="Children Under Thirteen",
        description="Data relating to children under the age of thirteen.",
        parent_key="user.children",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.children.thirteen_to_sixteen",
        name="Children Thirteen to Sixteen",
        description="Data relating to children between the ages of thirteen and sixteen.",
        parent_key="user.children",
        version_added="3.2.0",
    ),
    ################
    # user.contact #
    ################
    default_category_factory(
        fides_key="user.contact",
        name="Contact Data",
        description="Contact data collected about a user.",
        parent_key="user",
    ),
    default_category_factory(
        fides_key="user.contact.address",
        name="User Contact Address",
        description="Contact address data collected about a user.",
        parent_key="user.contact",
    ),
    default_category_factory(
        fides_key="user.contact.address.city",
        name="User Contact City",
        description="User's city level address data.",
        parent_key="user.contact.address",
    ),
    default_category_factory(
        fides_key="user.contact.address.country",
        name="User Contact Country",
        description="User's country level address data.",
        parent_key="user.contact.address",
    ),
    default_category_factory(
        fides_key="user.contact.email",
        name="User Contact Email",
        description="User's contact email address.",
        parent_key="user.contact",
    ),
    default_category_factory(
        fides_key="user.contact.phone_number",
        name="User Contact Phone Number",
        description="User's phone number.",
        parent_key="user.contact",
    ),
    default_category_factory(
        fides_key="user.contact.url",
        name="User Website",
        description="Subject's websites or links to social and personal profiles.",
        parent_key="user.contact",
        version_deprecated="3.2.0",
        replaced_by="user.contact.social_url",
    ),
    default_category_factory(
        fides_key="user.contact.social_url",
        name="Social Media URL",
        description="Subject's websites or links to social and personal profiles.",
        parent_key="user.contact",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.contact.fax_number",
        name="Fax Number",
        description="Data Subject's fax number.",
        parent_key="user.contact",
    ),
    default_category_factory(
        fides_key="user.contact.address.postal_code",
        name="User Contact Postal Code",
        description="User's postal code.",
        parent_key="user.contact.address",
    ),
    default_category_factory(
        fides_key="user.contact.address.state",
        name="User Contact State",
        description="User's state level address data.",
        parent_key="user.contact.address",
    ),
    default_category_factory(
        fides_key="user.contact.address.street",
        name="User Contact Street",
        description="User's street level address data.",
        parent_key="user.contact.address",
    ),
    default_category_factory(
        fides_key="user.contact.address.mailing_address",
        name="Mailing Address",
        description="User's mailing address information.",
        parent_key="user.contact.address",
        version_added="3.2.0",
    ),
    # MERGED: user.contact.organization merged into user.contact
    default_category_factory(
        fides_key="user.contact.organization",
        name="Organization",
        description="Data Subject's Organization.",
        parent_key="user.contact",
        version_deprecated="3.2.0",
        replaced_by="user.contact",
    ),
    ################
    # user.content #
    ################
    default_category_factory(
        fides_key="user.content",
        name="User Content",
        description="Content related to, or created by the subject.",
        parent_key="user",
    ),
    default_category_factory(
        fides_key="user.content.private",
        name="Private Content",
        description="Private content related to, or created by the subject, not publicly available.",
        parent_key="user.content",
    ),
    default_category_factory(
        fides_key="user.content.public",
        name="Public Content",
        description="Publicly shared Content related to, or created by the subject.",
        parent_key="user.content",
    ),
    default_category_factory(
        fides_key="user.content.self_image",
        name="User Image",
        description="Photograph or image in which subject is whole or partially recognized.",
        parent_key="user.content",
    ),
    ####################
    # user.demographic #
    ####################
    default_category_factory(
        fides_key="user.demographic",
        name="Demographic Data",
        description="Demographic data about a user.",
        parent_key="user",
    ),
    default_category_factory(
        fides_key="user.demographic.age_range",
        name="Age Range",
        description="Non specific age or age-range of data subject.",
        parent_key="user.demographic",
    ),
    default_category_factory(
        fides_key="user.demographic.date_of_birth",
        name="Birth Date",
        description="Date of birth of data subject.",
        parent_key="user.demographic",
    ),
    default_category_factory(
        fides_key="user.demographic.gender",
        name="Gender",
        description="Gender of data subject.",
        parent_key="user.demographic",
    ),
    default_category_factory(
        fides_key="user.demographic.language",
        name="Language",
        description="Spoken or written language of subject.",
        parent_key="user.demographic",
    ),
    default_category_factory(
        fides_key="user.demographic.marital_status",
        name="Marital Status",
        description="Marital status of data subject.",
        parent_key="user.demographic",
    ),
    default_category_factory(
        fides_key="user.demographic.political_opinion",
        name="Political Opinion",
        description="Political opinion or belief of data subject.",
        parent_key="user.demographic",
    ),
    default_category_factory(
        fides_key="user.demographic.profile",
        name="User Profile Data",
        description="Profile or preference information about the data subject.",
        parent_key="user.demographic",
    ),
    default_category_factory(
        fides_key="user.demographic.race_ethnicity",
        name="Race",
        description="Race or ethnicity of data subject.",
        parent_key="user.demographic",
    ),
    default_category_factory(
        fides_key="user.demographic.religious_belief",
        name="Religion",
        description="Religion or religious beliefs of the data subject.",
        parent_key="user.demographic",
    ),
    default_category_factory(
        fides_key="user.demographic.sexual_orientation",
        name="Sexual Orientation",
        description="Sexual orientation of data subject.",
        parent_key="user.demographic",
    ),
    default_category_factory(
        fides_key="user.demographic.citizenship_or_immigration_status",
        name="Citizenship or Immigration Status",
        description="Citizenship or immigration status of data subject.",
        parent_key="user.demographic",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.demographic.philosophical_belief",
        name="Philosophical Belief",
        description="Philosophical beliefs or worldview of data subject.",
        parent_key="user.demographic",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.demographic.protected_classifications",
        name="Protected Classifications",
        description="Protected classifications or sensitive attributes of data subject.",
        parent_key="user.demographic",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.demographic.union_membership",
        name="Union Membership",
        description="Union membership status of data subject.",
        parent_key="user.demographic",
        version_added="3.2.0",
    ),
    #################
    # user.location #
    #################
    default_category_factory(
        fides_key="user.location",
        name="Location Data",
        description="Records of the location of a user.",
        parent_key="user",
    ),
    default_category_factory(
        fides_key="user.location.imprecise",
        name="Imprecise Subject Location",
        description="Imprecise location derived from sensors (more than 500M).",
        parent_key="user.location",
        version_deprecated="3.2.0",
        replaced_by="user.location.coarse",
    ),
    default_category_factory(
        fides_key="user.location.coarse",
        name="Coarse Subject Location",
        description="Coarse location derived from sensors (more than 500M).",
        parent_key="user.location",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.location.precise",
        name="Precise Subject Location",
        description="Precise location derived from sensors (less than 500M).",
        parent_key="user.location",
    ),
    ###############
    # user.device #
    ###############
    default_category_factory(
        fides_key="user.device",
        name="Device Data",
        description="Data related to a user's device, configuration and setting.",
        parent_key="user",
    ),
    default_category_factory(
        fides_key="user.device.cookie",
        name="Device Cookie",
        description="Data related to a subject, stored within a cookie.",
        parent_key="user.device",
    ),
    default_category_factory(
        fides_key="user.device.cookie_id",
        name="Cookie ID",
        description="Cookie unique identification number.",
        parent_key="user.device",
    ),
    default_category_factory(
        fides_key="user.device.device_id",
        name="Device ID",
        description="Device unique identification number.",
        parent_key="user.device",
    ),
    default_category_factory(
        fides_key="user.device.ip_address",
        name="IP Address",
        description="Unique identifier related to device connection.",
        parent_key="user.device",
    ),
    default_category_factory(
        fides_key="user.device.sensor",
        name="Device Sensor Data",
        description="Measurement data from device sensors and monitoring systems.",
        parent_key="user.device",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.device.telemetry",
        name="Device Telemetry",
        description="User identifiable measurement data from device sensors and monitoring.",
        parent_key="user.device",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.payment",
        name="Payment Data",
        description="Payment data related to user.",
        parent_key="user",
    ),
    default_category_factory(
        fides_key="user.social",
        name="Social Data",
        description="Social activity and interaction data.",
        parent_key="user",
        version_deprecated="3.2.0",
        replaced_by="user.social_activity",
    ),
    default_category_factory(
        fides_key="user.social_activity",
        name="Social Activity Data",
        description="Social activity and interaction data.",
        parent_key="user",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.settings",
        name="User Settings",
        description="User preferences and settings data.",
        parent_key="user",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.unique_id",
        name="Unique ID",
        description="Unique identifier for a user assigned through system use.",
        parent_key="user",
    ),
    # MERGED: user.unique_id.pseudonymous merged into user.unique_id
    default_category_factory(
        fides_key="user.unique_id.pseudonymous",
        name="Pseudonymous User ID",
        description="A pseudonymous, or probabilistic identifier generated from other subject or device data belonging to the subject.",
        parent_key="user.unique_id",
        version_deprecated="3.2.0",
        replaced_by="user.unique_id",
    ),
    default_category_factory(
        fides_key="user.unique_id.deterministic",
        name="Deterministic User ID",
        description="A deterministic identifier that can be consistently generated from user data.",
        parent_key="user.unique_id",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.unique_id.probablistic",
        name="Probabilistic User ID",
        description="A probabilistic identifier generated from other subject or device data.",
        parent_key="user.unique_id",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.telemetry",
        name="Telemetry Data",
        description="User identifiable measurement data from system sensors and monitoring.",
        parent_key="user",
        version_deprecated="3.2.0",
        replaced_by="user.device.telemetry",
    ),
    # MERGED: user.user_sensor merged into user.device.sensor
    default_category_factory(
        fides_key="user.user_sensor",
        name="User Sensor Data",
        description="Measurement data about a user's environment through system use.",
        parent_key="user",
        version_deprecated="3.2.0",
        replaced_by="user.device.sensor",
    ),
    default_category_factory(
        fides_key="user.sensor",
        name="Sensor Data",
        description="Measurement data from sensors and monitoring systems.",
        parent_key="user",
        version_deprecated="3.2.0",
        replaced_by="user.device.sensor",
    ),
    ##################
    # user.financial #
    ##################
    default_category_factory(
        fides_key="user.financial",
        name="Financial Data",
        description="Payment data and financial history.",
        parent_key="user",
    ),
    default_category_factory(
        fides_key="user.financial.bank_account",
        name="Bank Account Information",
        description="Bank account information belonging to the subject.",
        parent_key="user.financial",
    ),
    default_category_factory(
        fides_key="user.financial.credit_card",
        name="Credit Card Information",
        description="Credit card information belonging to the subject.",
        parent_key="user.financial",
    ),
    ######################
    # user.government_id #
    ######################
    default_category_factory(
        fides_key="user.government_id",
        name="Government ID",
        description="State provided identification data.",
        parent_key="user",
    ),
    default_category_factory(
        fides_key="user.government_id.birth_certificate",
        name="Birth Certificate",
        description="State issued certificate of birth.",
        parent_key="user.government_id",
    ),
    default_category_factory(
        fides_key="user.government_id.drivers_license_number",
        name="Driver's License Number",
        description="State issued driving identification number.",
        parent_key="user.government_id",
    ),
    default_category_factory(
        fides_key="user.government_id.immigration",
        name="Immigration ID",
        description="State issued immigration or residency data.",
        parent_key="user.government_id",
    ),
    default_category_factory(
        fides_key="user.government_id.national_identification_number",
        name="National Identification Number",
        description="State issued personal identification number.",
        parent_key="user.government_id",
    ),
    default_category_factory(
        fides_key="user.government_id.passport_number",
        name="Passport Number",
        description="State issued passport data.",
        parent_key="user.government_id",
    ),
    default_category_factory(
        fides_key="user.government_id.vehicle_registration",
        name="Vehicle Registration",
        description="State issued license plate or vehicle registration data.",
        parent_key="user.government_id",
    ),
    ###########################
    # user.health_and_medical #
    ###########################
    default_category_factory(
        fides_key="user.health_and_medical",
        name="Health and Medical Data",
        description="Health records or individual's personal medical information.",
        parent_key="user",
        version_deprecated="3.2.0",
        replaced_by="user.health",
    ),
    ##############
    # user.health #
    ##############
    default_category_factory(
        fides_key="user.health",
        name="Health Data",
        description="Health records or individual's personal medical information.",
        parent_key="user",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.health_and_medical.genetic",
        name="User's Genetic Data",
        description="Data about the genetic makeup provided by the subject.",
        parent_key="user.health_and_medical",
        version_deprecated="3.2.0",
        replaced_by="user.health.genetic",
    ),
    default_category_factory(
        fides_key="user.health.genetic",
        name="Genetic Data",
        description="Data about the genetic makeup provided by the subject.",
        parent_key="user.health",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.health_and_medical.insurance_beneficiary_id",
        name="Medical Insurance ID",
        description="Health insurance beneficiary number of the subject.",
        parent_key="user.health_and_medical",
        version_deprecated="3.2.0",
        replaced_by="user.health.insurance_beneficiary_id",
    ),
    default_category_factory(
        fides_key="user.health.insurance_beneficiary_id",
        name="Health Insurance ID",
        description="Health insurance beneficiary number of the subject.",
        parent_key="user.health",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.health_and_medical.record_id",
        name="Medical Record ID",
        description="Medical record identifiers belonging to a subject.",
        parent_key="user.health_and_medical",
        version_deprecated="3.2.0",
        replaced_by="user.health.record_id",
    ),
    default_category_factory(
        fides_key="user.health.record_id",
        name="Health Record ID",
        description="Medical record identifiers belonging to a subject.",
        parent_key="user.health",
        version_added="3.2.0",
    ),
    # New health categories added in 3.2.0
    default_category_factory(
        fides_key="user.health.baby_formula",
        name="Baby Formula Information",
        description="Information about baby formula usage or preferences.",
        parent_key="user.health",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.health.condition",
        name="Health Condition",
        description="Health condition or status information.",
        parent_key="user.health",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.health.maternity_clothing",
        name="Maternity Clothing",
        description="Information about maternity clothing purchases or preferences.",
        parent_key="user.health",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.health.medical_diagnosis",
        name="Medical Diagnosis",
        description="Medical diagnosis information.",
        parent_key="user.health",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.health.medications",
        name="Medications",
        description="Information about medications.",
        parent_key="user.health",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.health.prescriptions",
        name="Prescriptions",
        description="Prescription medication information.",
        parent_key="user.health",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.health.reproductive_or_sexual",
        name="Reproductive or Sexual Health",
        description="Reproductive or sexual health information.",
        parent_key="user.health",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.health.social_psychological_behavioral",
        name="Social, Psychological, or Behavioral Health",
        description="Social, psychological, or behavioral health information.",
        parent_key="user.health",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.health.symptons",
        name="Health Symptoms",
        description="Health symptom information.",
        parent_key="user.health",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.health.treatment",
        name="Medical Treatment",
        description="Medical treatment information.",
        parent_key="user.health",
        version_added="3.2.0",
    ),
    #############
    # user.name #
    #############
    default_category_factory(
        fides_key="user.name",
        name="Name",
        description="User's real name.",
        parent_key="user",
    ),
    default_category_factory(
        fides_key="user.name.first",
        name="First Name",
        description="Subject's first name.",
        parent_key="user.name",
    ),
    default_category_factory(
        fides_key="user.name.last",
        name="Last Name",
        description="Subject's last, or family, name.",
        parent_key="user.name",
    ),
    ###############
    # user.<misc> #
    ###############
    default_category_factory(
        fides_key="user.criminal_history",
        name="Criminal History",
        description="Criminal records or information about the data subject.",
        parent_key="user",
    ),
    default_category_factory(
        fides_key="user.privacy_preferences",
        name="Privacy Preferences",
        description="Privacy preferences or settings set by the subject.",
        parent_key="user",
    ),
    default_category_factory(
        fides_key="user.job_title",
        name="Job Title",
        description="Professional data.",
        parent_key="user",
        version_deprecated="3.2.0",
        replaced_by="user.professional_information.job_title",
    ),
    default_category_factory(
        fides_key="user.workplace",
        name="Workplace",
        description="Organization of employment.",
        parent_key="user",
        version_deprecated="3.2.0",
        replaced_by="user.professional_information.workplace",
    ),
    ##################################
    # user.professional_information #
    ##################################
    default_category_factory(
        fides_key="user.professional_information",
        name="Professional Information",
        description="Professional and employment-related information.",
        parent_key="user",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.professional_information.job_title",
        name="Professional Job Title",
        description="Professional job title or position.",
        parent_key="user.professional_information",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="user.professional_information.workplace",
        name="Professional Workplace",
        description="Organization or workplace of employment.",
        parent_key="user.professional_information",
        version_added="3.2.0",
    ),
    default_category_factory(
        fides_key="system",
        name="System Data",
        description="Data unique to, and under control of the system.",
    ),
    default_category_factory(
        fides_key="system.authentication",
        name="Authentication Data",
        description="Data used to manage access to the system.",
        parent_key="system",
    ),
    default_category_factory(
        fides_key="system.operations",
        name="Operations Data",
        description="Data used for system operations.",
        parent_key="system",
    ),
]
