#!/usr/bin/python3

from colorama import Fore, Back, Style

maximum_number = 10000

def getDividers(value):

   # print('\nReference Number ' + str(value))
    dividers = []

    for i in range(1, value):
        remainder = value % i
      #  print(str(value) + ' / ' + str(i) + ' has remainder ' + str(remainder))
        if remainder == 0:
            dividers.append(i)

    return dividers

def isPerfect(value):

    dividers = getDividers(value)
    sum_of_dividers = sum(dividers)
    if sum_of_dividers == value:
        return True
    else:
        return False

def main():
    print("Starting to compute perfect numbers up to " + str(maximum_number))

    for i in range(1, maximum_number):
        if isPerfect(i):
            print('Number ' + str(i) + ' is perfect.')

if __name__ == "__main__":
    main()



#https://www.youtube.com/watch?v=BfoWo4wFfcE&list=PLQN09mzV5mbLK9OvKQf1ZfXpPlBi461zp&index=3&ab_channel=MiguelArmandoRiemdeOliveira
