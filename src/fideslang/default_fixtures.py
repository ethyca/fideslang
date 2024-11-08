"""
This is a slowly changing dataset built from a public endpoint
and stored here as a constant to reduce non-value added api calls.

https://restcountries.com/v2/all?fields=name,alpha3Code

To update:
1. Make a GET request to the above url
2. Copy/Paste the JSON response below
"""

COUNTRY_CODES = [
    {"name": "Afghanistan", "alpha3Code": "AFG"},
    {"name": "Åland Islands", "alpha3Code": "ALA"},
    {"name": "Albania", "alpha3Code": "ALB"},
    {"name": "Algeria", "alpha3Code": "DZA"},
    {"name": "American Samoa", "alpha3Code": "ASM"},
    {"name": "Andorra", "alpha3Code": "AND"},
    {"name": "Angola", "alpha3Code": "AGO"},
    {"name": "Anguilla", "alpha3Code": "AIA"},
    {"name": "Antarctica", "alpha3Code": "ATA"},
    {"name": "Antigua and Barbuda", "alpha3Code": "ATG"},
    {"name": "Argentina", "alpha3Code": "ARG"},
    {"name": "Armenia", "alpha3Code": "ARM"},
    {"name": "Aruba", "alpha3Code": "ABW"},
    {"name": "Australia", "alpha3Code": "AUS"},
    {"name": "Austria", "alpha3Code": "AUT"},
    {"name": "Azerbaijan", "alpha3Code": "AZE"},
    {"name": "Bahamas", "alpha3Code": "BHS"},
    {"name": "Bahrain", "alpha3Code": "BHR"},
    {"name": "Bangladesh", "alpha3Code": "BGD"},
    {"name": "Barbados", "alpha3Code": "BRB"},
    {"name": "Belarus", "alpha3Code": "BLR"},
    {"name": "Belgium", "alpha3Code": "BEL"},
    {"name": "Belize", "alpha3Code": "BLZ"},
    {"name": "Benin", "alpha3Code": "BEN"},
    {"name": "Bermuda", "alpha3Code": "BMU"},
    {"name": "Bhutan", "alpha3Code": "BTN"},
    {"name": "Bolivia (Plurinational State of)", "alpha3Code": "BOL"},
    {"name": "Bonaire, Sint Eustatius and Saba", "alpha3Code": "BES"},
    {"name": "Bosnia and Herzegovina", "alpha3Code": "BIH"},
    {"name": "Botswana", "alpha3Code": "BWA"},
    {"name": "Bouvet Island", "alpha3Code": "BVT"},
    {"name": "Brazil", "alpha3Code": "BRA"},
    {"name": "British Indian Ocean Territory", "alpha3Code": "IOT"},
    {"name": "United States Minor Outlying Islands", "alpha3Code": "UMI"},
    {"name": "Virgin Islands (British)", "alpha3Code": "VGB"},
    {"name": "Virgin Islands (U.S.)", "alpha3Code": "VIR"},
    {"name": "Brunei Darussalam", "alpha3Code": "BRN"},
    {"name": "Bulgaria", "alpha3Code": "BGR"},
    {"name": "Burkina Faso", "alpha3Code": "BFA"},
    {"name": "Burundi", "alpha3Code": "BDI"},
    {"name": "Cambodia", "alpha3Code": "KHM"},
    {"name": "Cameroon", "alpha3Code": "CMR"},
    {"name": "Canada", "alpha3Code": "CAN"},
    {"name": "Cabo Verde", "alpha3Code": "CPV"},
    {"name": "Cayman Islands", "alpha3Code": "CYM"},
    {"name": "Central African Republic", "alpha3Code": "CAF"},
    {"name": "Chad", "alpha3Code": "TCD"},
    {"name": "Chile", "alpha3Code": "CHL"},
    {"name": "China", "alpha3Code": "CHN"},
    {"name": "Christmas Island", "alpha3Code": "CXR"},
    {"name": "Cocos (Keeling) Islands", "alpha3Code": "CCK"},
    {"name": "Colombia", "alpha3Code": "COL"},
    {"name": "Comoros", "alpha3Code": "COM"},
    {"name": "Congo", "alpha3Code": "COG"},
    {"name": "Congo (Democratic Republic of the)", "alpha3Code": "COD"},
    {"name": "Cook Islands", "alpha3Code": "COK"},
    {"name": "Costa Rica", "alpha3Code": "CRI"},
    {"name": "Croatia", "alpha3Code": "HRV"},
    {"name": "Cuba", "alpha3Code": "CUB"},
    {"name": "Curaçao", "alpha3Code": "CUW"},
    {"name": "Cyprus", "alpha3Code": "CYP"},
    {"name": "Czech Republic", "alpha3Code": "CZE"},
    {"name": "Denmark", "alpha3Code": "DNK"},
    {"name": "Djibouti", "alpha3Code": "DJI"},
    {"name": "Dominica", "alpha3Code": "DMA"},
    {"name": "Dominican Republic", "alpha3Code": "DOM"},
    {"name": "Ecuador", "alpha3Code": "ECU"},
    {"name": "Egypt", "alpha3Code": "EGY"},
    {"name": "El Salvador", "alpha3Code": "SLV"},
    {"name": "Equatorial Guinea", "alpha3Code": "GNQ"},
    {"name": "Eritrea", "alpha3Code": "ERI"},
    {"name": "Estonia", "alpha3Code": "EST"},
    {"name": "Ethiopia", "alpha3Code": "ETH"},
    {"name": "Falkland Islands (Malvinas)", "alpha3Code": "FLK"},
    {"name": "Faroe Islands", "alpha3Code": "FRO"},
    {"name": "Fiji", "alpha3Code": "FJI"},
    {"name": "Finland", "alpha3Code": "FIN"},
    {"name": "France", "alpha3Code": "FRA"},
    {"name": "French Guiana", "alpha3Code": "GUF"},
    {"name": "French Polynesia", "alpha3Code": "PYF"},
    {"name": "French Southern Territories", "alpha3Code": "ATF"},
    {"name": "Gabon", "alpha3Code": "GAB"},
    {"name": "Gambia", "alpha3Code": "GMB"},
    {"name": "Georgia", "alpha3Code": "GEO"},
    {"name": "Germany", "alpha3Code": "DEU"},
    {"name": "Ghana", "alpha3Code": "GHA"},
    {"name": "Gibraltar", "alpha3Code": "GIB"},
    {"name": "Greece", "alpha3Code": "GRC"},
    {"name": "Greenland", "alpha3Code": "GRL"},
    {"name": "Grenada", "alpha3Code": "GRD"},
    {"name": "Guadeloupe", "alpha3Code": "GLP"},
    {"name": "Guam", "alpha3Code": "GUM"},
    {"name": "Guatemala", "alpha3Code": "GTM"},
    {"name": "Guernsey", "alpha3Code": "GGY"},
    {"name": "Guinea", "alpha3Code": "GIN"},
    {"name": "Guinea-Bissau", "alpha3Code": "GNB"},
    {"name": "Guyana", "alpha3Code": "GUY"},
    {"name": "Haiti", "alpha3Code": "HTI"},
    {"name": "Heard Island and McDonald Islands", "alpha3Code": "HMD"},
    {"name": "Vatican City", "alpha3Code": "VAT"},
    {"name": "Honduras", "alpha3Code": "HND"},
    {"name": "Hungary", "alpha3Code": "HUN"},
    {"name": "Hong Kong", "alpha3Code": "HKG"},
    {"name": "Iceland", "alpha3Code": "ISL"},
    {"name": "India", "alpha3Code": "IND"},
    {"name": "Indonesia", "alpha3Code": "IDN"},
    {"name": "Ivory Coast", "alpha3Code": "CIV"},
    {"name": "Iran (Islamic Republic of)", "alpha3Code": "IRN"},
    {"name": "Iraq", "alpha3Code": "IRQ"},
    {"name": "Ireland", "alpha3Code": "IRL"},
    {"name": "Isle of Man", "alpha3Code": "IMN"},
    {"name": "Israel", "alpha3Code": "ISR"},
    {"name": "Italy", "alpha3Code": "ITA"},
    {"name": "Jamaica", "alpha3Code": "JAM"},
    {"name": "Japan", "alpha3Code": "JPN"},
    {"name": "Jersey", "alpha3Code": "JEY"},
    {"name": "Jordan", "alpha3Code": "JOR"},
    {"name": "Kazakhstan", "alpha3Code": "KAZ"},
    {"name": "Kenya", "alpha3Code": "KEN"},
    {"name": "Kiribati", "alpha3Code": "KIR"},
    {"name": "Kuwait", "alpha3Code": "KWT"},
    {"name": "Kyrgyzstan", "alpha3Code": "KGZ"},
    {"name": "Lao People's Democratic Republic", "alpha3Code": "LAO"},
    {"name": "Latvia", "alpha3Code": "LVA"},
    {"name": "Lebanon", "alpha3Code": "LBN"},
    {"name": "Lesotho", "alpha3Code": "LSO"},
    {"name": "Liberia", "alpha3Code": "LBR"},
    {"name": "Libya", "alpha3Code": "LBY"},
    {"name": "Liechtenstein", "alpha3Code": "LIE"},
    {"name": "Lithuania", "alpha3Code": "LTU"},
    {"name": "Luxembourg", "alpha3Code": "LUX"},
    {"name": "Macao", "alpha3Code": "MAC"},
    {"name": "North Macedonia", "alpha3Code": "MKD"},
    {"name": "Madagascar", "alpha3Code": "MDG"},
    {"name": "Malawi", "alpha3Code": "MWI"},
    {"name": "Malaysia", "alpha3Code": "MYS"},
    {"name": "Maldives", "alpha3Code": "MDV"},
    {"name": "Mali", "alpha3Code": "MLI"},
    {"name": "Malta", "alpha3Code": "MLT"},
    {"name": "Marshall Islands", "alpha3Code": "MHL"},
    {"name": "Martinique", "alpha3Code": "MTQ"},
    {"name": "Mauritania", "alpha3Code": "MRT"},
    {"name": "Mauritius", "alpha3Code": "MUS"},
    {"name": "Mayotte", "alpha3Code": "MYT"},
    {"name": "Mexico", "alpha3Code": "MEX"},
    {"name": "Micronesia (Federated States of)", "alpha3Code": "FSM"},
    {"name": "Moldova (Republic of)", "alpha3Code": "MDA"},
    {"name": "Monaco", "alpha3Code": "MCO"},
    {"name": "Mongolia", "alpha3Code": "MNG"},
    {"name": "Montenegro", "alpha3Code": "MNE"},
    {"name": "Montserrat", "alpha3Code": "MSR"},
    {"name": "Morocco", "alpha3Code": "MAR"},
    {"name": "Mozambique", "alpha3Code": "MOZ"},
    {"name": "Myanmar", "alpha3Code": "MMR"},
    {"name": "Namibia", "alpha3Code": "NAM"},
    {"name": "Nauru", "alpha3Code": "NRU"},
    {"name": "Nepal", "alpha3Code": "NPL"},
    {"name": "Netherlands", "alpha3Code": "NLD"},
    {"name": "New Caledonia", "alpha3Code": "NCL"},
    {"name": "New Zealand", "alpha3Code": "NZL"},
    {"name": "Nicaragua", "alpha3Code": "NIC"},
    {"name": "Niger", "alpha3Code": "NER"},
    {"name": "Nigeria", "alpha3Code": "NGA"},
    {"name": "Niue", "alpha3Code": "NIU"},
    {"name": "Norfolk Island", "alpha3Code": "NFK"},
    {"name": "Korea (Democratic People's Republic of)", "alpha3Code": "PRK"},
    {"name": "Northern Mariana Islands", "alpha3Code": "MNP"},
    {"name": "Norway", "alpha3Code": "NOR"},
    {"name": "Oman", "alpha3Code": "OMN"},
    {"name": "Pakistan", "alpha3Code": "PAK"},
    {"name": "Palau", "alpha3Code": "PLW"},
    {"name": "Palestine, State of", "alpha3Code": "PSE"},
    {"name": "Panama", "alpha3Code": "PAN"},
    {"name": "Papua New Guinea", "alpha3Code": "PNG"},
    {"name": "Paraguay", "alpha3Code": "PRY"},
    {"name": "Peru", "alpha3Code": "PER"},
    {"name": "Philippines", "alpha3Code": "PHL"},
    {"name": "Pitcairn", "alpha3Code": "PCN"},
    {"name": "Poland", "alpha3Code": "POL"},
    {"name": "Portugal", "alpha3Code": "PRT"},
    {"name": "Puerto Rico", "alpha3Code": "PRI"},
    {"name": "Qatar", "alpha3Code": "QAT"},
    {"name": "Republic of Kosovo", "alpha3Code": "UNK"},
    {"name": "Réunion", "alpha3Code": "REU"},
    {"name": "Romania", "alpha3Code": "ROU"},
    {"name": "Russian Federation", "alpha3Code": "RUS"},
    {"name": "Rwanda", "alpha3Code": "RWA"},
    {"name": "Saint Barthélemy", "alpha3Code": "BLM"},
    {"name": "Saint Helena, Ascension and Tristan da Cunha", "alpha3Code": "SHN"},
    {"name": "Saint Kitts and Nevis", "alpha3Code": "KNA"},
    {"name": "Saint Lucia", "alpha3Code": "LCA"},
    {"name": "Saint Martin (French part)", "alpha3Code": "MAF"},
    {"name": "Saint Pierre and Miquelon", "alpha3Code": "SPM"},
    {"name": "Saint Vincent and the Grenadines", "alpha3Code": "VCT"},
    {"name": "Samoa", "alpha3Code": "WSM"},
    {"name": "San Marino", "alpha3Code": "SMR"},
    {"name": "Sao Tome and Principe", "alpha3Code": "STP"},
    {"name": "Saudi Arabia", "alpha3Code": "SAU"},
    {"name": "Senegal", "alpha3Code": "SEN"},
    {"name": "Serbia", "alpha3Code": "SRB"},
    {"name": "Seychelles", "alpha3Code": "SYC"},
    {"name": "Sierra Leone", "alpha3Code": "SLE"},
    {"name": "Singapore", "alpha3Code": "SGP"},
    {"name": "Sint Maarten (Dutch part)", "alpha3Code": "SXM"},
    {"name": "Slovakia", "alpha3Code": "SVK"},
    {"name": "Slovenia", "alpha3Code": "SVN"},
    {"name": "Solomon Islands", "alpha3Code": "SLB"},
    {"name": "Somalia", "alpha3Code": "SOM"},
    {"name": "South Africa", "alpha3Code": "ZAF"},
    {"name": "South Georgia and the South Sandwich Islands", "alpha3Code": "SGS"},
    {"name": "Korea (Republic of)", "alpha3Code": "KOR"},
    {"name": "Spain", "alpha3Code": "ESP"},
    {"name": "Sri Lanka", "alpha3Code": "LKA"},
    {"name": "Sudan", "alpha3Code": "SDN"},
    {"name": "South Sudan", "alpha3Code": "SSD"},
    {"name": "Suriname", "alpha3Code": "SUR"},
    {"name": "Svalbard and Jan Mayen", "alpha3Code": "SJM"},
    {"name": "Swaziland", "alpha3Code": "SWZ"},
    {"name": "Sweden", "alpha3Code": "SWE"},
    {"name": "Switzerland", "alpha3Code": "CHE"},
    {"name": "Syrian Arab Republic", "alpha3Code": "SYR"},
    {"name": "Taiwan", "alpha3Code": "TWN"},
    {"name": "Tajikistan", "alpha3Code": "TJK"},
    {"name": "Tanzania, United Republic of", "alpha3Code": "TZA"},
    {"name": "Thailand", "alpha3Code": "THA"},
    {"name": "Timor-Leste", "alpha3Code": "TLS"},
    {"name": "Togo", "alpha3Code": "TGO"},
    {"name": "Tokelau", "alpha3Code": "TKL"},
    {"name": "Tonga", "alpha3Code": "TON"},
    {"name": "Trinidad and Tobago", "alpha3Code": "TTO"},
    {"name": "Tunisia", "alpha3Code": "TUN"},
    {"name": "Turkey", "alpha3Code": "TUR"},
    {"name": "Turkmenistan", "alpha3Code": "TKM"},
    {"name": "Turks and Caicos Islands", "alpha3Code": "TCA"},
    {"name": "Tuvalu", "alpha3Code": "TUV"},
    {"name": "Uganda", "alpha3Code": "UGA"},
    {"name": "Ukraine", "alpha3Code": "UKR"},
    {"name": "United Arab Emirates", "alpha3Code": "ARE"},
    {
        "name": "United Kingdom of Great Britain and Northern Ireland",
        "alpha3Code": "GBR",
    },
    {"name": "United States of America", "alpha3Code": "USA"},
    {"name": "Uruguay", "alpha3Code": "URY"},
    {"name": "Uzbekistan", "alpha3Code": "UZB"},
    {"name": "Vanuatu", "alpha3Code": "VUT"},
    {"name": "Venezuela (Bolivarian Republic of)", "alpha3Code": "VEN"},
    {"name": "Vietnam", "alpha3Code": "VNM"},
    {"name": "Wallis and Futuna", "alpha3Code": "WLF"},
    {"name": "Western Sahara", "alpha3Code": "ESH"},
    {"name": "Yemen", "alpha3Code": "YEM"},
    {"name": "Zambia", "alpha3Code": "ZMB"},
    {"name": "Zimbabwe", "alpha3Code": "ZWE"},
]
