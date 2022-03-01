"""Testing the Calculator"""
from calculator.operations import Subtraction, Multiplication, Addition


def test_calculator_add_method():
    """Testing the Calculator"""
    assert Addition.add(1,1) == 2

def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    assert Subtraction.subtract(1,1) == 0

def test_calculator_multiply_method():
    """Testing the Calculator Subtract"""
    assert Multiplication.multiply(1,1) == 1