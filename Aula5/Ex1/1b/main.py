#!/usr/bin/python3

import cv2
import argparse
import time
import colorama
import cv2

def main():

    parser = argparse.ArgumentParser(description='Opencv example')
    parser.add_argument('--image1', type=str, help='Path to image')
    args = vars(parser.parse_args())
    print(args)

    image = cv2.imread(args['image1'], cv2.IMREAD_COLOR)  # Load an image
    cv2.imshow('window', image)  # Display the image

    # '/home/vinicius/Desktop/PSR_Git/psr_21-22/Parte05/images/atlas2000_e_atlasmv.png'

    cv2.waitKey(1000) # Show the images just for 1 second

if __name__ == '__main__':
    main()

