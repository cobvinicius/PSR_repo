#!/usr/bin/python3

import cv2
import os

# https://techvidvan.com/tutorials/face-recognition-project-python-opencv/

def main():

    # Initialize the classifier:
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # initial setup
    capture = cv2.VideoCapture(0)
    window_name = 'Detetar imagem'

    while (True):

        # Capture the video frame
        ret, frame = capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow(window_name, frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    capture.release()

    # Destroy all the windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()