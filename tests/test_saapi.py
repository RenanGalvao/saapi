import re
import pytest
from saapi import SaAPI
from saapi.countries import Country


def test_saapi():
    saapi_client = SaAPI({
        "app_id": "",
        "secret": "",
    })
    assert len(re.findall(f"\\.{Country.BRAZIL}/", saapi_client.url)) == 1

    saapi_client = SaAPI({
        "app_id": "",
        "secret": "",
        "country": Country.MALAYSIA
    })
    assert len(re.findall(f"\\.{Country.MALAYSIA}/", saapi_client.url)) == 1

    with pytest.raises(ValueError):
        SaAPI({
            "app_id": "",
            "secret": "",
            "country": ".org"
        })
