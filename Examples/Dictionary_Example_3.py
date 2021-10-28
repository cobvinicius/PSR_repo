#!/usr/bin/python3
import json

from colorama import Fore, Back, Style
import argparse
import readchar

def main():

    d = {'name': 'UA', 'Country': 'Portugal', 'Districts': ['Porto', 'Aveiro'], 'Persons': [{'name': 'Antonio'}, {'name': 'Maria'}]}
    print(d)

    print(json.dumps(d, sort_keys=True, indent = 8))

if __name__ == "__main__":
        main()