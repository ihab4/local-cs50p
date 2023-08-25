from plates import is_valid


def test_min_max():
    assert is_valid("ab") == False
    assert is_valid("a1") == False
    assert is_valid("abcdefg") == False


def test_numberInMiddle():
    assert is_valid("aa22aa") == False


def test_zero():
    assert is_valid("0abc") == False


def test_ponct_space():
    assert is_valid("a,b 0?1") == False


def test_valid():
    assert is_valid("aaa222") == True
    assert is_valid("aa22") == True