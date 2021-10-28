#!/usr/bin/python3

import readchar
from colorama import Fore, Back, Style
from time import time, ctime
import math
from time import time

def tic():
    """
    Functions used to return the numbers of seconds passed since epoch to use with function toc() afterwards.
    Like tic toc matlab functions.
    :return: a float.
    """

    global start_time
    start_time = time()


def toc():
    """
    Function used to print the elapsed time since function tic() was used. tic() and toc() works together.
    :return: a float.
    """

    # Get the number os seconds passed since epoch and subtract from tic(). This is the elapsed time from tic to toc.

    # Check if start_time is inside global variables
    if 'start_time' in globals():
        last_time = time()
        elapsed_time = last_time - start_time
        print('Elapsed time: ' + str(elapsed_time) + ' seconds.')
    else:
        print('Error: start time from tic() not set')

def main():

    # Get current date and print it using colorama.
    current_date = ctime()
    print('This is ' + Fore.RED + 'Ex1 ' + Fore.RESET + 'and the current date is ' + Fore.BLUE + Back.LIGHTYELLOW_EX
          + current_date + Style.RESET_ALL)

    # Make a cycle to calculate the elapse time.
    maximum_number = int(50e6)

    tic()
    for i in range(0, maximum_number):
        math.sqrt(i)

    toc()

if __name__ == "__main__":
    main()

