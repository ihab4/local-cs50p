from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(6)
    assert jar.capacity == 6

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(11)
    assert jar.size == 12


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(1)
    assert jar.size == 11
    jar.withdraw(11)
    assert jar.size == 0

def test_errors():
    jar = Jar(6)
    with pytest.raises(ValueError):
        jar.withdraw(1)
        jar.deposit(7)
