#!/usr/bin/python3

import cv2
import argparse
import time
import colorama


def main():

    # Process arguments
    parser = argparse.ArgumentParser(description='Opencv example')
    parser.add_argument('--image1', type=str, help='Path to image')

    # Load image
    image_original = cv2.imread(args['image1'], cv2.IMREAD_COLOR) # Load an image
    image_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)

    # Process image
    


    image_filename = '/psr_21-22/Parte05/images/atlas2000_e_atlasmv.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR) # Load an image

    cv2.imshow('window', image)  # Display the image
    cv2.waitKey(0) # wait for a key press before proceeding


if __name__ == '__main__':
    main()
