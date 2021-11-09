#!/usr/bin/python3

import cv2
import argparse
import time
import colorama


def main():

    # '/home/vinicius/Desktop/PSR_Git/psr_21-22/Parte05/images/atlascar2.png'

    # Process arguments
    parser = argparse.ArgumentParser(description='Opencv example')
    parser.add_argument('--image1', type=str, help='Path to image')
    args = vars(parser.parse_args())

    # Load image
    image_rgb = cv2.imread(args['image1'], cv2.IMREAD_COLOR)  # Load an image
    image_b, image_g, image_r = cv2.split(image_rgb) # Separate the channels (in OpenCV the representation is BGR)

    print('image_rgb shape ' + str(image_rgb.shape))
    print('image_r shape ' + str(image_r.shape))   # -> 1 channel image, so can be binarized

    # Process image
    retval, image_b_processed = cv2.threshold(image_b, 50, 255, cv2.THRESH_BINARY)   # binarize blue channel
    retval, image_g_processed = cv2.threshold(image_g, 100, 255, cv2.THRESH_BINARY)  # binarize green channel
    retval, image_r_processed = cv2.threshold(image_r, 150, 255, cv2.THRESH_BINARY)  # binarize red channel

    new_image_rgb = cv2.merge((image_b_processed, image_g_processed, image_r_processed)) # merge the processed images
    
    # Visualization
    cv2.imshow('original', image_rgb) # Display the original image
    cv2.imshow('processed b', image_b_processed) # Display the processed blue channel image
    cv2.imshow('processed g', image_g_processed) # Display the processed green channel image
    cv2.imshow('processed r', image_r_processed)  # Display the processed red channel image
    cv2.imshow('new_image_rgb', new_image_rgb)  # Display the processed new image

    cv2.waitKey(0) # wait for a key press before proceding

if __name__ == '__main__':
    main()
