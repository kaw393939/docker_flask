""" This is the Calculator Class"""
from calculator.calculation import Addition, Subtraction, Multiplication

class Calculator:
    """ This is the default result property"""
    @staticmethod
    def add(tuple):
        """ This is the add method"""
        # Call the static method add to return the sum and set it to the calculator result property
        calculation = Addition.create(tuple)
        return calculation.get_result()

    @staticmethod
    def subtract(tuple):
        """ This is the subtract method"""
        calculation = Subtraction.create(tuple)
        return calculation.get_result()
    @staticmethod
    def multiply(tuple):
        """ This is the subtract method"""
        calculation = Multiplication.create(tuple)
        return calculation.get_result()

