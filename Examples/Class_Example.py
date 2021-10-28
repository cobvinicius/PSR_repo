#!/usr/bin/python3

from colorama import Fore, Back, Style
import argparse
import readchar


class Person:
    def __init__(self, name, address, phone):

        # Cria as variaveis para poder utiliza-las depois
        self.name = name
        self.address = address
        self.phone = phone

        def __str__(self):
            return 'Name: ' + self.name + ' address: ' + self.address + ' phone: ' + str(self.phone)

def main():

    jose = Person('Jose', 'Aveiro', 93)
    miguel = Person('Miguel', 'Ilhavo', 91)

    print(jose)

    miguel.name += jose.name
    print(miguel)


if __name__ == "__main__":
        main()