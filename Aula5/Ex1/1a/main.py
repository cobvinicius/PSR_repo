#!/usr/bin/python3

import cv2
import argparse
import time
import colorama
import cv2

def main():

    image_filename = '/home/vinicius/Desktop/PSR_Git/psr_21-22/Parte05/images/atlas2000_e_atlasmv.png' # Image path
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    cv2.imshow('window', image)  # Display the image

    image_bright = image + 20 # image brighter (overflow)
   # image_bright = image - 50  # Should be darker but the type image is an uint8 and doesnt represent negative numbers -> underflow
    cv2.imshow('window2', image_bright)

    cv2.waitKey(0) # wait for a key press before proceeding

if __name__ == '__main__':
    main()

