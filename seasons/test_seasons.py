from seasons import calcul, convert_minutes
from datetime import date


def test_calcul():
    assert calcul(date.fromisoformat("2000-01-01")) == ((date.today() - date.fromisoformat("2000-01-01")).days) * 24 * 60


def test_convert():
    assert convert_minutes(525600) == "Five hundred twenty-five thousand, six hundred minutes"


def test_both():
    assert convert_minutes(calcul(date.fromisoformat("2022-01-01"))) == "Eight hundred ninety-five thousand, six hundred eighty minutes"