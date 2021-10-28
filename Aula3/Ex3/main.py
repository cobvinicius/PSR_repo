#!/usr/bin/python3

from colorama import Fore, Back, Style
import argparse
import readchar

Complex = namedtuple('Complex', ['r', 'i'])

def addComplex(x, y):
    """
    Add complex number x and y and return it.
    :param x: A complex number given in as a namedtuple of size two. The first element is the real part and the second is
              the imaginary part.
    :param y: A complex number given in as a namedtuple of size two. The first element is the real part and the second is
              the imaginary part.
    :return: real and imaginary parts as namedtuple.
    """

    # Option A: without using complex built-in function.
    # Get real and imaginary parts of the complex number given
    real_x, imag_x = x.r, x.i
    real_y, imag_y = y.r, y.i

    # Add the real parts and the imaginary parts separately
    real_part = real_x + real_y
    imag_part = imag_x + imag_y

    return Complex(r=real_part, i=imag_part)

    # # Option B: using complex built-in function
    # # Convert x and y to complex numbers
    # x = complex(x.r, x.i)
    # y = complex(y.r, y.i)
    #
    # # Add the complex numbers.
    # result = x + y
    # real_part = result.real
    # imag_part = result.imag
    #
    # return Complex(r=real_part, i=imag_part)


def multiplyComplex(x, y):
    """
    Multiply complex number x and y and return it.
    :param x: A complex number given in as a namedtuple of size two. The first element is the real part and the second is
              the imaginary part.
    :param y: A complex number given in as a namedtuple of size two. The first element is the real part and the second is
              the imaginary part.
    :return: real and imaginary parts as namedtuple.
    """

    # Option A: without using complex built-in function.
    # Get real and imaginary parts of the complex number given
    real_x, imag_x = x.r, x.i
    real_y, imag_y = y.r, y.i

    # Multiply each part of the first complex by each part of the second complex number
    firsts = real_x * real_y
    outers = real_x * imag_y
    inners = imag_x * real_y
    lasts = imag_x * imag_y

    # Calculate the real and the imaginary parts
    real_part = firsts - lasts
    imag_part = outers + inners

    return Complex(r=real_part, i=imag_part)

    # # Option B: using complex built-in function
    # # Convert x and y to complex numbers
    # x = complex(x.r, x.i)
    # y = complex(y.r, y.i)
    #
    # # Multiply the complex numbers.
    # result = x * y
    # real_part = result.real
    # imag_part = result.imag
    #
    # return Complex(r=real_part, i=imag_part)


def printComplex(x, prefix=''):
    """
    Print a complex numbers
    :param x: A complex number given in as a namedtuple of size two. The first element is the real part and the second is
              the imaginary part.
    """

    # Get real and imaginary parts of the complex number given
    real_x, imag_x = x.r, x.i

    print(prefix + str(real_x) + ' + ' + str(imag_x) + 'i')


def main():
    # define two complex numbers as namedtuple of size two
    c1 = Complex(r=5, i=3)
    c2 = Complex(r=-2, i=7)

    # See how namedtuple Complex prints
    print('namedtuple c1 = ' + str(c1))
    print('namedtuple c2 = ' + str(c2))

    # Test addComplex function
    c3 = addComplex(c1, c2)
    printComplex(c3, 'c1 + c2 = ')

    # Test multiplyComplex function
    c4 = multiplyComplex(c1, c2)
    printComplex(c4, 'c1 * c2 = ')


if __name__ == "__main__":
    main()

