"""Testing the Calculator"""
# From specifies the namespace
from calculator.calculation import Addition, Subtraction, Multiplication


def test_calculation_multiplication_instance():
    """Testing the Calculator Subtract"""
    tuple = (1, 2)
    calculation = Multiplication.create(tuple)
    assert isinstance(calculation, Multiplication)


def test_calculation_subtraction_instance():
    """Testing the Calculator Subtract"""
    tuple = (1, 2)
    calculation = Subtraction.create(tuple)
    assert isinstance(calculation, Subtraction)


def test_calculation_addition_instance():
    """Testing the Calculator Subtract"""
    tuple = (1, 2)
    calculation = Addition.create(tuple)
    assert isinstance(calculation, Addition)


def test_calculation_add_method():
    """Testing the Calculator"""
    # this is show using the calculator object add method
    tuple = (1, 2)
    calculation = Addition.create(tuple)
    assert calculation.get_result() == 3


def test_calculation_subtract_method():
    """Testing the Calculator Subtract"""
    tuple = (1, 2)
    calculation = Subtraction.create(tuple)
    assert calculation.get_result() == -3


def test_calculation_multiply_method():
    """Testing the Calculator Subtract"""
    tuple = (1, 2)
    calculation = Multiplication.create(tuple)
    assert calculation.get_result() == 2
