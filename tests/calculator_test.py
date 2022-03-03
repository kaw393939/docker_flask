"""Testing the Calculator"""
# From specifies the namespace
from calculator import Calculator


def test_calculator_add_method():
    """Testing the Calculator"""
    # this is show using the calculator object add method
    tuple = (1,2)
    assert Calculator.add(tuple) == 3

def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    tuple = (1,2)
    assert Calculator.subtract(tuple) == -3


def test_calculator_multiply_method():
    """Testing the Calculator Subtract"""
    tuple = (1,2)
    assert Calculator.multiply(tuple) == 2
