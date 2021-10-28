#!/usr/bin/python3

from colorama import Fore, Back, Style
import argparse
import readchar


def add(x, y):

    real_x = x['r']
    imag_x = x['i']
    real_y = y['r']
    imag_y = y['i']

    real_part = real_x + real_y
    imag_part = imag_x + imag_y

    return {'r': real_part, 'i': imag_part}


def main():

    dict_complexs = {}

    # Dictionary:
    # Class:

    dict_complexs['add'] = add
    dict_complexs['c1'] = {'r': 5, 'i': 3}
    dict_complexs['c2'] = {'r': 3, 'i': -7}
    dict_complexs['c3'] = dict_complexs['add'](dict_complexs['c1'], dict_complexs['c2'])

    print(dict_complexs)
    print(dict_complexs['c1'])
    print(dict_complexs['c2'])
    print(dict_complexs['c3'])

if __name__ == "__main__":
        main()