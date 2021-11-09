#!/usr/bin/python3
import copy

import cv2
import argparse
import time
import colorama
import numpy as np

# /home/vinicius/Desktop/PSR_Git/psr_21-22/Parte05/images/atlascar.png

def main():

    # Process arguments
    parser = argparse.ArgumentParser(description='Opencv example')
    parser.add_argument('--image1', required= True, type=str, help='Path to image')
    args = vars(parser.parse_args())

    # Load image
    image = cv2.imread(args['image1'], cv2.IMREAD_COLOR)  # Load an image

    # Image processing
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # To find the centroid, the image needs to be grayscaled
    moment = cv2.moments(gray_img)

    # Find the centroid
    X = int(moment["m10"] / moment["m00"])
    Y = int(moment["m01"] / moment["m00"])

    # Draw a circle
    cv2.circle(image, (X, Y), 50, (255, 0, 0), 1)

    # Write a sentence (1 - b)
    text = 'PSR'
    cv2.putText(image, text, (500, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 2, cv2.LINE_AA, False)  # image, text, org, font, fontScale, color, thickness, cv2.LINE_AA, True

    # Show the image with the circle
    cv2.imshow("Center of the Image", image)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
