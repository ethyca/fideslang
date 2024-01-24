import pytest

from fideslang.gvl import (
    GVL_FEATURES,
    GVL_SPECIAL_FEATURES,
    Feature,
    data_category_id_to_data_categories,
    data_use_to_purpose,
    feature_id_to_feature_name,
    feature_name_to_feature,
    purpose_to_data_use,
)


def test_purpose_to_data_use():
    assert purpose_to_data_use(1) == ["functional.storage"]
    assert purpose_to_data_use(1, False) == [
        "functional.storage"
    ]  # assert False is the default

    # testing special purpose lookup
    assert purpose_to_data_use(1, True) == [
        "essential.fraud_detection",
        "essential.service.security",
    ]

    # let's test one other purpose just to be comprehensive
    assert purpose_to_data_use(4) == [
        "marketing.advertising.first_party.targeted",
        "marketing.advertising.third_party.targeted",
    ]

    assert purpose_to_data_use(11) == ["personalize.content.limited"]

    # assert invalid uses raise KeyErrors
    with pytest.raises(KeyError):
        purpose_to_data_use(12)

    with pytest.raises(KeyError):
        purpose_to_data_use(3, True)


def test_data_use_to_purpose():
    purpose_1 = data_use_to_purpose("functional.storage")
    assert purpose_1
    assert purpose_1.id == 1
    assert purpose_1.name == "Store and/or access information on a device"
    assert (
        purpose_1.description
        == "Cookies, device or similar online identifiers (e.g. login-based identifiers, randomly assigned identifiers, network based identifiers) together with other information (e.g. browser type and information, language, screen size, supported technologies etc.) can be stored or read on your device to recognise it each time it connects to an app or to a website, for one or several of the purposes presented here."
    )
    assert purpose_1.illustrations == [
        "Most purposes explained in this notice rely on the storage or accessing of information from your device when you use an app or visit a website. For example, a vendor or publisher might need to store a cookie on your device during your first visit on a website, to be able to recognise your device during your next visits (by accessing this cookie each time)."
    ]

    # ensure that english is the same as no language/default
    assert data_use_to_purpose("functional.storage", "en") == purpose_1

    # and ensure we can get another language
    purpose_1_spanish = data_use_to_purpose("functional.storage", "es")
    assert purpose_1_spanish
    assert purpose_1_spanish.id == 1
    assert (
        purpose_1_spanish.name
        == "Almacenar la información en un dispositivo y/o acceder a ella"
    )
    assert (
        purpose_1_spanish.description
        == "Las cookies, los identificadores de dispositivos o los identificadores online de similares características (p. ej., los identificadores basados en inicio de sesión, los identificadores asignados aleatoriamente, los identificadores basados en la red), junto con otra información (p. ej., la información y el tipo del navegador, el idioma, el tamaño de la pantalla, las tecnologías compatibles, etc.), pueden almacenarse o leerse en tu dispositivo a fin de reconocerlo siempre que se conecte a una aplicación o a una página web para una o varias de los finalidades que se recogen en el presente texto."
    )
    assert purpose_1_spanish.illustrations == [
        "La mayoría de las finalidades que se explican en este texto dependen del almacenamiento o del acceso a la información de tu dispositivo cuando utilizas una aplicación o visitas una página web. Por ejemplo, es posible que un proveedor o un editor/medio de comunicación necesiten almacenar una cookie en tu dispositivo la primera vez que visite una página web a fin de poder reconocer tu dispositivo las próximas veces que vuelva a visitarla (accediendo a esta cookie cada vez que lo haga)."
    ]

    # testing special purpose lookup
    special_purpose_1 = data_use_to_purpose("essential.fraud_detection")
    assert special_purpose_1.id == 1
    assert (
        special_purpose_1.name
        == "Ensure security, prevent and detect fraud, and fix errors"
    )
    assert (
        special_purpose_1.description
        == "Your data can be used to monitor for and prevent unusual and possibly fraudulent activity (for example, regarding advertising, ad clicks by bots), and ensure systems and processes work properly and securely. It can also be used to correct any problems you, the publisher or the advertiser may encounter in the delivery of content and ads and in your interaction with them."
    )
    assert special_purpose_1.illustrations == [
        "An advertising intermediary delivers ads from various advertisers to its network of partnering websites. It notices a large increase in clicks on ads relating to one advertiser, and uses data regarding the source of the clicks to determine that 80% of the clicks come from bots rather than humans."
    ]

    # ensure that english is the same as no language/default
    assert data_use_to_purpose("essential.fraud_detection", "en") == special_purpose_1

    # and ensure we can get another language
    special_purpose_1_french = data_use_to_purpose("essential.fraud_detection", "fr")
    assert special_purpose_1_french.id == 1
    assert (
        special_purpose_1_french.name
        == "Assurer la sécurité, prévenir et détecter la fraude et réparer les erreurs"
    )
    assert (
        special_purpose_1_french.description
        == "Vos données peuvent être utilisées pour surveiller et prévenir les activités inhabituelles et potentiellement frauduleuses (par exemple, en ce qui concerne la publicité, les clics publicitaires par des robots), et s’assurer que les systèmes et processus fonctionnent correctement et en toute sécurité. Elles peuvent également être utilisées pour corriger les problèmes que vous, l’éditeur ou l’annonceur pouvez rencontrer dans la diffusion de contenus et de publicités et dans votre interaction avec ceux-ci.",
    )
    assert special_purpose_1_french.illustrations == [
        "Un intermédiaire publicitaire diffuse des publicités de divers annonceurs sur son réseau de sites Web partenaires. Il remarque une augmentation importante des clics sur les publicités relatives à un annonceur, et utilise les données concernant la source des clics pour établir que 80 % des clics proviennent de robots plutôt que d’êtres humains."
    ]

    # assert invalid data use returns None
    data_use_to_purpose("bogus_use") is None


def test_features():
    """Add a sanity check for features and special features parsing"""
    assert isinstance(GVL_FEATURES[1]["en"], Feature)
    assert (
        GVL_FEATURES[1]["en"].name == "Match and combine data from other data sources"
    )

    assert isinstance(GVL_SPECIAL_FEATURES[1]["en"], Feature)
    assert GVL_SPECIAL_FEATURES[1]["en"].name == "Use precise geolocation data"


def test_feature_name_to_feature():
    assert feature_name_to_feature("Link different devices").id == 2
    assert feature_name_to_feature("Use precise geolocation data").id == 1
    assert feature_name_to_feature("Name doesn't exist") is None


def test_feature_id_to_feature_name():
    assert (
        feature_id_to_feature_name(feature_id=1)
        == "Match and combine data from other data sources"
    )
    assert (
        feature_id_to_feature_name(feature_id=1, special_feature=True)
        == "Use precise geolocation data"
    )

    assert feature_id_to_feature_name(feature_id=1001) is None


def test_data_category_id_to_data_categories():
    assert data_category_id_to_data_categories(1) == ["user.device.ip_address"]

    # let's test one other data category just to be comprehensive
    assert data_category_id_to_data_categories(5) == [
        "user.account",
        "user.unique_id",
        "user.device",
    ]

    # assert invalid categories raise KeyErrors
    with pytest.raises(KeyError):
        data_category_id_to_data_categories(12)
