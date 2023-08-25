from twttr import shorten


def test_withoutVowel():
    assert shorten("twttr") == "twttr"


def test_lower():
    assert shorten("twitter") == "twttr"


def test_upper():
    assert shorten("TWITTER") == "TWTTR"


def test_Capital():
    assert shorten("Twitter") == "Twttr"


def test_withoutLowerVowel():
    assert shorten("twIttEr") == "twttr"


def test_number():
    assert shorten("123") == "123"


def test_ponctu():
    assert shorten(",./?!") == ",./?!"