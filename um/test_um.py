from um import count


def test_um_space():
    assert count("hello um world um") == 2
    assert count("um thanks um for the album.") == 2


def test_upperCase():
    assert count("hello, Um world uM ") == 2
    assert count("UM thanks for the album.") == 1


def test_ponctu():
    assert count("hello, um, world.um.") == 2
    assert count("um?thanks, um, for the album. um.") == 2


def test_null():
    assert count("helloum, worldum.") == 0
    assert count("thanksum, for the album.") == 0