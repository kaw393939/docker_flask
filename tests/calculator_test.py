"""Testing the Calculator"""
# From specifies the namespace
from calculator import Calculator


def test_calculator_add_method():
    """Testing the Calculator"""
    # this is show using the calculator object add method
    tuple_list = (1,2)
    assert Calculator.add(tuple_list) == 3

def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    tuple_list = (1,2)
    assert Calculator.subtract(tuple_list) == -3


def test_calculator_multiply_method():
    """Testing the Calculator Subtract"""
    tuple_list = (1,2)
    assert Calculator.multiply(tuple_list) == 2
