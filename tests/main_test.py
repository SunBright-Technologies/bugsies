from bugsies.main import DEFAULT_FORMAT, create_bugsie, create_versioned_bugsie, get_bugsie, get_bugsie_with_format
from bugsies.models import SupportedFormat


def test_create_bugsie():
    res = create_bugsie()
    assert res["message"] == "Placeholder: create bugsie"
    assert res["version"] == "v1"
    assert res["seed"] == ""


def test_create_versioned_bugsie():
    res = create_versioned_bugsie("v2")
    assert res["message"] == "Placeholder: create bugsie"
    assert res["version"] == "v2"
    assert res["seed"] == ""


def test_get_bugsie():
    res = get_bugsie("any_id")
    assert res["message"] == "Placeholder: get bugsie"
    assert res["id"] == res["id"]
    assert res["format"] == DEFAULT_FORMAT


def test_get_bugsie_with_format():
    res = get_bugsie_with_format("any_id", SupportedFormat.PNG)
    assert res["message"] == "Placeholder: get bugsie"
    assert res["id"] == res["id"]
    assert res["format"] == SupportedFormat.PNG
