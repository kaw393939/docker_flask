""" This is the Calculator Class"""
from calculator.calculations import Addition, Subtraction, Multiplication


class Calculator:
    """ This is the default result property"""

    @staticmethod
    def add(tuple_list):
        """ This is the add method"""
        # Call the static method add to return the sum and set it to the calculator result property
        calculation = Addition.create(tuple_list)
        return calculation.get_result()

    @staticmethod
    def subtract(tuple_list):
        """ This is the subtract method"""
        calculation = Subtraction.create(tuple_list)
        return calculation.get_result()

    @staticmethod
    def multiply(tuple_list):
        """ This is the subtract method"""
        calculation = Multiplication.create(tuple_list)
        return calculation.get_result()
