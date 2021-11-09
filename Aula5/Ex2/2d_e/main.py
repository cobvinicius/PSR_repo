#!/usr/bin/python3
import copy

import cv2
import argparse
import time
import colorama
import numpy as np


# /home/vinicius/Desktop/PSR_Git/psr_21-22/Parte05/images/atlas2000_e_atlasmv.png

def main():

    # Process arguments
    parser = argparse.ArgumentParser(description='Opencv example')
    parser.add_argument('--image1', required= True, type=str, help='Path to image')
    args = vars(parser.parse_args())

    # Load image
    image_rgb = cv2.imread(args['image1'], cv2.IMREAD_COLOR)  # Load an image
    image_b, image_g, image_r = cv2.split(image_rgb)


    # Dictionary ranges of each channel
 #   ranges = {'b': {'min': 20, 'max': 150},
 #             'g': {'min': 20, 'max': 150},
 #             'r': {'min': 20, 'max': 150}}

    # Show the green block as white
    ranges = {'b': {'min': 0, 'max': 100},
              'g': {'min': 80, 'max': 256},
              'r': {'min': 0, 'max': 100}}


    # Process image
    mins = np.array([ranges['b']['min'], ranges['g']['min'], ranges['r']['min']]) # Converts the dictionary representation in np.array, which is the representation required by the inRange function
    maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])
    # image_processed = cv2.inRange(image_rgb, mins, maxs)
    mask = cv2.inRange(image_rgb, mins, maxs) # Mask to detect the green box

    # Convert from uint8 to boolean using numpy
    mask = mask.astype(np.bool)


    image_processed = copy.deepcopy(image_rgb)
    #image_processed[mask] = (image_processed[mask]*0.4).astype(np.uint8) # Pixels selected by the mask become darker -> Green box becomes darker
    #image_processed[np.logical_not(mask)] = (image_processed[np.logical_not(mask)]*0.4).astype(np.uint8) # Do the oposite: Everything but gree box become darker
    image_processed[mask] = (0,255,0) # Paint the green box of pure green

    # Show the data type of each images (elements inside the images)
    print(image_rgb.dtype)
    print(mask.dtype)
    print(image_processed.dtype)


    # Visualization
    cv2.namedWindow('original', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('original', image_rgb)  # Display the original image
    cv2.imshow('mask' , mask.astype(np.uint8)*255) # imshow doenst recognize the boolean type image. So, to display the image, it is necessary to reconvert the mask to uint8
    cv2.imshow('processed image', image_processed)  # Display the processed image

    cv2.waitKey(0)  # wait for a key press before proceding


if __name__ == '__main__':
    main()
