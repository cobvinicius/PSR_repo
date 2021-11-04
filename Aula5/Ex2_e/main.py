#!/usr/bin/python3

import cv2
import argparse
import time
import colorama
import numpy as np


def main():
    # Process arguments
    parser = argparse.ArgumentParser(description='Opencv example')
    parser.add_argument('--image1', required= True, type=str, help='Path to image')
    args = vars(parser.parse_args())

    # Load image
    image_rgb = cv2.imread(args['image1'], cv2.IMREAD_COLOR)  # Load an image
    image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2HSV)
    image_h, image_s, image_v = cv2.split(image_rgb)


    # Show the green block as white
    ranges = {'h': {'min': 0, 'max': 100},
              's': {'min': 80, 'max': 256},
              'v': {'min': 0, 'max': 100}}


    # Process image

    mins = np.array([ranges['h']['min'], ranges['s']['min'], ranges['v']['min']])
    maxs = np.array([ranges['h']['max'], ranges['s']['max'], ranges['v']['max']])
    image_processed = cv2.inRange(image_hsv, mins, maxs)


    # Visualization
    cv2.namedWindow('original', cv2.WINDOW_AUTOSIZE)
#  cv2.imshow('original', image_rgb)  # Display the image
    cv2.imshow('original', image_hsv)  # Display the image
    cv2.imshow('image_processed' , image_processed)  # Display the image

    cv2.waitKey(0)  # wait for a key press before proceding


if __name__ == '__main__':
    main()