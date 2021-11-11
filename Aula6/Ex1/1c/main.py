#!/usr/bin/python3

import cv2
import numpy as np


click = False

def onMouse(cursor, xposition, yposition, flags, param):

    global click
    if cursor == cv2.EVENT_LBUTTONDOWN:
        click = True
     #   param[yposition, xposition] = color
        cv2.circle(param, (xposition, yposition), 10, color, -1)

    elif cursor == cv2.EVENT_MOUSEMOVE and click == True:
        # param[yposition, xposition] = color
         cv2.circle(param, (xposition, yposition), 10, color, -1)

    elif cursor == cv2.EVENT_LBUTTONUP:
        click = False


def main():

    whiteboard = np.ones((800, 800, 3),np.uint8)*255
    window_name = 'Pynting'

    global color
    color = (0, 0, 0)  # set black as default

    while True:
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        cv2.imshow(window_name, whiteboard)

        key = cv2.waitKey(10)

        if key == ord('r'):
            color = (0, 0, 255)
        elif key == ord('g'):
            color = (0, 255, 0)
        elif key == ord('b'):
            color = (255, 0, 0)
        elif key == ord('q'):
            break

        cv2.setMouseCallback(window_name, onMouse, param=whiteboard)


if __name__ == "__main__":
    main()