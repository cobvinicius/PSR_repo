#!/usr/bin/python3

from colorama import Fore, Back, Style
import argparse
import readchar


class Complex:
    def __init__(self, r, i):
        """
        Class to represent complex numbers.
        :param r: real part of the complex number.
        :param i: imaginary part of the complex number.
        """

        self.r = r  # store real part in class instance
        self.i = i  # store imaginary part in class instance

    def add(self, y):
        """
        Function to add the complex number class object to other complex number class object given.
        :param y: Complex number class object
        """

        # Add the real parts and the imaginary parts separately and store in class instances
        self.r = self.r + y.r
        self.i = self.i + y.i

        return Complex(r=self.r, i=self.i)

    def multiply(self, y):
        """
        Function to multiply the complex number class object to other complex number class object given.
        :param y: Complex number class object
        """

        # Multiply each part of the complex number class object by each part of the second complex number given
        firsts = self.r * y.r
        outers = self.r * y.i
        inners = self.i * y.r
        lasts = self.i * y.i

        # Calculate the real and the imaginary parts and store in class instances
        self.r = firsts - lasts
        self.i = outers + inners

        return Complex(r=self.r, i=self.i)

    def __str__(self):
        """
        Complex number representation.
        :return: string
        """
        return str(self.r) + ' + ' + str(self.i) + 'i'

def main():
        # define two complex numbers class objects
        c1 = Complex(r=5, i=3)
        c2 = Complex(r=-2, i=7)

        print('c1: ' + str(c1))
        print('c2: ' + str(c2))

        # Test add returning a new complex number class object.
        c3 = c1.add(c2)
        print('c1 + c2: ' + str(c3))

        # ---------------------------------------------------------------------------

        # define two complex numbers class objects
        c1 = Complex(r=5, i=3)
        c2 = Complex(r=-2, i=7)

        # Test add without returning anything
        c1.add(c2)
        print('c1 + c2: ' + str(c1))

        # ---------------------------------------------------------------------------

        # define two complex numbers class objects
        c1 = Complex(r=5, i=3)
        c2 = Complex(r=-2, i=7)

        # Test multiply returning a new complex number class object.
        c4 = c1.multiply(c2)
        print('c1 * c2: ' + str(c4))

        # ---------------------------------------------------------------------------

        # define two complex numbers class objects
        c1 = Complex(r=5, i=3)
        c2 = Complex(r=-2, i=7)

        # Test multiply without returning anything
        c1.multiply(c2)
        print('c1 * c2: ' + str(c1))

if __name__ == "__main__":
        main()