#!/usr/bin/python3

import copy
import argparse
import cv2
import numpy as np
from functools import partial

# /home/vinicius/Desktop/PSR_Git/psr_21-22/Parte05/images/atlas2000_e_atlasmv.png

def onTrackbarBH():

def onTrackbarGS():

def onTrackbarRV():



def main():

    # parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-img', '--image', type=str, required=True, help='Full path to image file.')
    parser.add_argument('-hsv ', '--hue_saturation_value', help='To modify the image using HSV instead of BGR',
                        action='store_true')
    args = vars(parser.parse_args())

    # Window name definition
    window_name = 'window - Ex3d'

    # Load and show the image
    image = cv2.imread(args['image'], cv2.IMREAD_COLOR)
    cv2.namedWindow(window_name)
    cv2.imshow(window_name, image)

    # Converts rbg image to hsv image if hsv was chosen
    if args['hsv']:
        image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


###############################################################################################################

    # Separate the channels
    image_b, image_g, image_r = cv2.split(image)


    ranges = {'limits': {'BH': {'max': 200, 'min': 100},
                         'GS': {'max': 200, 'min': 100},
                         'RV': {'max': 200, 'min': 100}}}

    # Process image
    mins = np.array([ranges['b']['min'], ranges['g']['min'], ranges['r']['min']]) # Converts the dictionary representation in np.array, which is the representation required by the inRange function
    maxs = np.array([ranges['b']['max'], ranges['g']['max'], ranges['r']['max']])
    mask = cv2.inRange(image, mins, maxs) # Mask to detect the green box

    TB_PF_BH_Min = partial(onTrackbar, window_name=window_name, image_gray=image_gray, )
    cv2.createTrackbar('Min range B/H', window_name, 0, 255, TB_PF_BH_Min)

    cv2.createTrackbar('Max range B/H', window_name, 0, 255, TracBar_PartFunc)



if __name__ == '__main__':
    main()