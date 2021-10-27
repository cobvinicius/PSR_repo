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

    count_pressed_numbers = 0
    count_pressed_others = 0

    while True:
        print('\nType something (X to stop)')
        pressed_key = readchar.readkey()

        if str.isnumeric(pressed_key):
            count_pressed_numbers +=1
        else:
            count_pressed_others +=1

        if pressed_key == stop_char:
            print('You typed ' + pressed_key + ' terminating.')
            break

        else:
            print('Thank you for typing ' + pressed_key)

    print('You entered ' + str(count_pressed_numbers) + ' numbers.')
    print('You entered ' + str(count_pressed_others) + ' others.')


def main():

    #Ex 4)a)
    #print('Give me the stop char ')
    #pressed_char = readchar.readchar()
    #printAllCharsUpTo(pressed_char)

    #Ex 4)b) c)
    readAllUpTo('X')

if __name__ == "__main__":
    main()



# https://www.youtube.com/watch?v=ANOpVGbaHe0&list=PLQN09mzV5mbLK9OvKQf1ZfXpPlBi461zp&index=4&t=23s&ab_channel=MiguelArmandoRiemdeOliveira
# https://www.youtube.com/watch?v=PEME9k1WaZY&list=PLQN09mzV5mbLK9OvKQf1ZfXpPlBi461zp&index=5&ab_channel=MiguelArmandoRiemdeOliveira
# https://www.youtube.com/watch?v=IHTIYJuLdnQ&list=PLQN09mzV5mbLK9OvKQf1ZfXpPlBi461zp&index=6&ab_channel=MiguelArmandoRiemdeOliveira

