#!/usr/bin/python3

import cv2
import argparse
import time
import colorama


def main():

    # '/home/vinicius/Desktop/PSR_Git/psr_21-22/Parte05/images/atlas2000_e_atlasmv.png'

    # Process arguments
    parser = argparse.ArgumentParser(description='Opencv example')
    parser.add_argument('--image1', type=str, help='Path to image')
    args = vars(parser.parse_args())
    print(args)


    # Load image
    image_original = cv2.imread(args['image1'], cv2.IMREAD_COLOR) # Load an image
    image_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY) # Converts an image in RGB to gray to be able to binarize

    # Process image
    # cv.threshold(src, thresh, maxval, type[,dst],  ) -> retval, dst
    retval, image_processed = cv2.threshold(image_gray, 128, 255, cv2.THRESH_BINARY)   # Binarization


    # Visualization
    cv2.imshow('original', image_original)  # Display original image
    cv2.imshow('gray', image_gray)  # Display gray image
    cv2.imshow('processed', image_processed) # Display processed image

    cv2.waitKey(15000) # wait for 15 seconds and close all

if __name__ == '__main__':
    main()
