#!/usr/bin/python3

import cv2
import argparse
import numpy as np
from functools import partial

# /home/vinicius/Desktop/PSR_Git/psr_21-22/Parte05/images/atlas2000_e_atlasmv.png


def onTrackbar(threshold, image_gray, window_name):

    # The value selected on trackbar is the binarization value
    _, img_thresholded = cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow(window_name, img_thresholded)


def onMouse(cursor, xposition, yposition, s1, s2):
    if cursor == 1:
       print('Your cursor is on: x = ' + str(xposition) + ', y= ' + str(yposition) + ')')


def main():

    # Parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    # Load the image
    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)

    # Converting image to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    window_name = 'window - Ex3b'
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image_gray)

    # Create a trackbar to choose the binarization value using a partial function
    TrackBarTitle = 'Threshold'
    TracBar_PartFunc = partial(onTrackbar, window_name=window_name, image_gray=image_gray,)
    cv2.createTrackbar(TrackBarTitle, window_name, 0, 255, TracBar_PartFunc)

    # Mouse callback to show the mouse coordinates
    cv2.setMouseCallback(window_name, onMouse)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()
