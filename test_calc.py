import pytest
import calc


def test_add():
    assert calc.add(1, 1) == 2
    assert calc.add(2, 2) == 4


def test_subtract():
    assert calc.subtract(2, 1) == 1
    assert calc.subtract(1, 2) == -1


def test_divide():
    assert calc.divide(4, 2) == 2
    assert calc.divide(1, 2) == 0.5
