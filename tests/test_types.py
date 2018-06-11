import pytest
from pyuml2.types import UnlimitedNatural, Integer, Boolean, Real


def test_unlimitedNatural():
    assert isinstance(5, UnlimitedNatural)
    assert isinstance('a', UnlimitedNatural) is False

    assert UnlimitedNatural.to_string(5) == '5'
    assert UnlimitedNatural.to_string(-5) == '*'

    assert UnlimitedNatural.from_string('*') == -1
    assert UnlimitedNatural.from_string('5') == 5

    with pytest.raises(Exception):
        UnlimitedNatural.from_string('abc')

    with pytest.raises(Exception):
        UnlimitedNatural.from_string('-5')


def test_integer():
    assert isinstance(5, Integer)
    assert isinstance('a', Integer) is False

    assert Integer.to_string(5) == '5'
    assert Integer.to_string(-5) == '-5'

    assert Integer.from_string('-1') == -1
    assert Integer.from_string('5') == 5
    with pytest.raises(Exception):
        Integer.from_string('abc')


def test_real():
    assert isinstance(5., Real)
    assert isinstance(5.2358, Real)
    assert isinstance('a', Real) is False

    assert Real.to_string(5.123) == '5.123'
    assert Real.to_string(-5) == '-5'

    assert Real.from_string('-1') == -1
    assert Real.from_string('5.123') == 5.123
    with pytest.raises(Exception):
        Real.from_string('abc')


def test_boolean():
    assert isinstance(True, Boolean)
    assert isinstance(False, Boolean)
    assert isinstance(5, Boolean) is False

    assert Boolean.to_string(True) == 'true'
    assert Boolean.to_string(False) == 'false'

    assert Boolean.from_string('true') is True
    assert Boolean.from_string('false') is False
