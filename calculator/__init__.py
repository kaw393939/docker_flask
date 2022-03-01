""" This is the Calculator Class"""
from calculator.operations import Addition, Subtraction, Multiplication


class Calculator:
    """ This is the default result property"""
    result = 0

    def add(self, value_1, value_2):
        """ This is the add method"""
        # Call the static method add to return the sum and set it to the calculator result property
        self.result = Addition.add(value_1, value_2)
        return self.result

    def subtract(self, value_1, value_2):
        """ This is the subtract method"""
        self.result = Subtraction.subtract(value_1, value_2)
        return self.result

    def multiply(self, value_1, value_2):
        """ This is the subtract method"""
        self.result = Multiplication.multiply(value_1, value_2)
        return self.result

    def get_result(self):
        """ This is the get result method"""
        return self.result
