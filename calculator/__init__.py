""" This is the Calculator Class"""
class Calculator:
    """ This is the default result property"""
    result = 0

    def add(self,x):
        self.result = self.result + x
        return self.result