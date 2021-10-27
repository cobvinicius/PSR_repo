#!/usr/bin/python3

from colorama import Fore, Back, Style
import argparse

def isPrime(value):
    print('\nChecking number ' + str(value))

    for i in range(2,value):
        remainder = value % i
        print(str(value) + ' / ' + str(i) + ' has remainder ' + str(remainder))
        if remainder == 0:
            return False

    return True

def main():

    parser = argparse.ArgumentParser(description='PSR argparse example')
    parser.add_argument('--maximum_number', type=int, help='Maximum number to search for primes.')
    parser.add_argument('--verbose', action='store_true', help='print stuff to the screen or not.')
    args = vars(parser.parse_args())
    print(args)


    print("Starting to compute prime numbers up to " + str(args['maximum_number']))
    count = 0
    for i in range(1, args['maximum_number']):
        if isPrime(i):
            count += 1
            print('Number ' + Fore.YELLOW + Back.GREEN + str(i) + Style.RESET_ALL + ' is prime.')
        else:
            print('Number ' + str(i) + ' is not prime.')
            pass
    if args['verbose']:
         print(Fore.BLUE + 'Between 1 and ' + str(args['maximum_number']) + ' are ' + str(count) + ' prime numbers' + Style.RESET_ALL)

if __name__ == "__main__":
    main()



# https://www.youtube.com/watch?v=ANOpVGbaHe0&list=PLQN09mzV5mbLK9OvKQf1ZfXpPlBi461zp&index=4&t=23s&ab_channel=MiguelArmandoRiemdeOliveira
