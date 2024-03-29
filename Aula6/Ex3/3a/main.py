#!/usr/bin/python3

import copy
import cv2
import numpy as np

# https://towardsdatascience.com/face-detection-in-2-minutes-using-opencv-python-90f89d7c0f81

def main():

    # Initialize the cascade:
    faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

    # initial setup
    capture = cv2.VideoCapture(0)
    window_name = 'Detetar imagem'

    while True:

        # Capture the video frame
        ret, frame = capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
     #   cv2.imshow(window_name, frame)

        height,width,_ = frame.shape
        image_gui = copy.deepcopy(frame)

        # Face detection #

        # Convert to grayscale
        image_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = faceCascade.detectMultiScale(image_gray, 1.1, 4)

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(image_gui, (x, y), (x + w, y + h), (255, 0, 0), 2)

            mask_face = np.ndarray((height,width), dtype=np.uint8) # create a mask same size as image
            mask_face.fill(0) # set image to all zeros
            mask_face = cv2.rectangle(mask_face, (x, y), (x+w, y+h), 255, -1) # draw blue rectangle around face

            ##image_gui[mask_face.astype(bool)] = (255,255,0)

            cv2.add(frame, (-10, 50, -10, 0), dst = image_gui, mask = mask_face) # paint face color green

        # Display
        cv2.imshow(window_name, image_gui)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # After the loop release the cap object
    capture.release()

    # Destroy all the windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()