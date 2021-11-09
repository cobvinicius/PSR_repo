#!/usr/bin/python3

import cv2
import argparse
import time
import colorama
import cv2

def main():

    image_filename = '/home/vinicius/Desktop/PSR_Git/psr_21-22/Parte05/images/atlascar.png' # Image path
    image_filename2 = '/home/vinicius/Desktop/PSR_Git/psr_21-22/Parte05/images/atlascar2.png'  # Image path
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image
    image2 = cv2.imread(image_filename2, cv2.IMREAD_COLOR)  # Load an image


    while True:
        cv2.imshow('window', image)  # Display the image
        cv2.waitKey(3000) # wait 3 seconds
        cv2.imshow('window', image2)  # Display the image 2
        cv2.waitKey(3000)  # wait 3 seconds

if __name__ == '__main__':
    main()
