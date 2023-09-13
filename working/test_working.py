from working import convert
import pytest


def test_without_min():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("7 PM to 9 AM") == "19:00 to 09:00"


def test_with_min():
    assert convert("9:30 AM to 5:50 PM") == "09:30 to 17:50"
    assert convert("10:20 PM to 9:59 AM") == "22:20 to 09:59"


def test_wrong_min():
    with pytest.raises(ValueError):
        convert("8:60 AM to 4:60 PM")
        convert("8:60 PM to 4:60 AM")


def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("13:00 AM to 19:60 PM")
        convert("21 PM to 22 AM")


def test_value():
    with pytest.raises(ValueError):
        convert("8:00 AM - 4:60 PM")
        convert("8 PM TO 4 AM")