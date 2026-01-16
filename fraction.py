# fraction.py
# This file defines a custom Fraction class using Python magic methods.
# You can import this class in any Python file and use Fraction as a datatype.

class Fraction:
    def __init__(self, n, d):
        """
        Constructor for Fraction class.
        n -> numerator
        d -> denominator
        """
        self.num = n
        self.den = d

    def __str__(self):
        """
        This magic method is called when you print the object.
        Example: print(f1) -> 1/2
        """
        return "{}/{}".format(self.num, self.den)

    def __add__(self, other):
        """
        Handles addition of two Fraction objects using + operator.
        """
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den
        return Fraction(temp_num, temp_den)

    def __sub__(self, other):
        """
        Handles subtraction of two Fraction objects using - operator.
        """
        temp_num = self.num * other.den - other.num * self.den
        temp_den = self.den * other.den
        return Fraction(temp_num, temp_den)

    def __mul__(self, other):
        """
        Handles multiplication of two Fraction objects using * operator.
        """
        temp_num = self.num * other.num
        temp_den = self.den * other.den
        return Fraction(temp_num, temp_den)

    def __truediv__(self, other):
        """
        Handles division of two Fraction objects using / operator.
        """
        temp_num = self.num * other.den
        temp_den = self.den * other.num
        return Fraction(temp_num, temp_den)
