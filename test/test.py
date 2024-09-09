# test_calculator.py
import pytest
from calc import sumar, restar

def test_sumar():
    assert sumar(1, 2) == 3
    assert sumar(-1, 1) == 0
    assert sumar(-1, -1) == -2

def test_restar():
    assert restar(2, 1) == 1
    assert restar(-1, 1) == -2
    assert restar(-1, -1) == 0
