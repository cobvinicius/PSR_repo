#!/usr/bin/python3
import cv2
import argparse
import numpy as np

# Global variables
window_name = 'window - Ex3a'
image_gray = None

# /home/vinicius/Desktop/PSR_Git/psr_21-22/Parte05/images/atlas2000_e_atlasmv.png


def onTrackbar(threshold):

    # The value selected on trackbar is the binarization value
    _, img_thresholded = cv2.threshold(image_gray, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow(window_name, img_thresholded)


def main():

    # Parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', type=str, required=True,help='Full path to image file.')
    args = vars(parser.parse_args())

    # Load an image
    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)

    # using a global variable and converting to gray (single channel)
    global image_gray
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image_gray)

    # Create a trackbar to choose the binarization value
    TrackBarTitle = 'Threshold'
    cv2.createTrackbar(TrackBarTitle, window_name, 0, 255, onTrackbar)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()
