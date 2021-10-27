#!/usr/bin/python3

from colorama import Fore, Back, Style
import argparse
import readchar

def printAllCharsUpTo(stop_char):

    print('I dont know how to do this yet')

    print('Printing all values up to stop_char ' + str(stop_char))
    for i in range(ord(' '), ord(stop_char)+1):
        print(chr(i))


def readAllUpTo(stop_char):

    #Ask for all the entries and put them in a list
    pressed_keys = [] #empty list to start with

    while True:
        print('\nType something (X to stop)')
        pressed_key = readchar.readkey()

        if pressed_key == stop_char:
            print('You typed ' + pressed_key + ' terminating.')
            break

        else:
            pressed_keys.append(pressed_key)

    print('The keys you pressed are: ' + str(pressed_keys))

    count_pressed_numbers = 0
    count_pressed_others = 0
    pressed_numbers = []
    pressed_others = []

    for pressed_key in pressed_keys:
        if str.isnumeric(pressed_key):
            count_pressed_numbers += 1
            pressed_numbers.append(pressed_key)  #acrescenta a variavel na lista
        else:
            count_pressed_others += 1
            pressed_others.append(pressed_key)

    print('You entered ' + str(count_pressed_numbers) + ' numbers :' + str(pressed_numbers))
    print('You entered ' + str(count_pressed_others) + ' others :' + str(pressed_others))


def main():

    readAllUpTo('X')

if __name__ == "__main__":
    main()



# https://www.youtube.com/watch?v=ANOpVGbaHe0&list=PLQN09mzV5mbLK9OvKQf1ZfXpPlBi461zp&index=4&t=23s&ab_channel=MiguelArmandoRiemdeOliveira
# https://www.youtube.com/watch?v=PEME9k1WaZY&list=PLQN09mzV5mbLK9OvKQf1ZfXpPlBi461zp&index=5&ab_channel=MiguelArmandoRiemdeOliveira
# https://www.youtube.com/watch?v=IHTIYJuLdnQ&list=PLQN09mzV5mbLK9OvKQf1ZfXpPlBi461zp&index=6&ab_channel=MiguelArmandoRiemdeOliveira

