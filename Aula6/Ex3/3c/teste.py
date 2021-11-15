#!/usr/bin/python3

import copy
import cv2
import numpy as np
import dlib

#https://livecodestream.dev/post/detecting-face-features-with-python/

def main():
    # Initialize the cascade:
    faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

    # initial setup
    capture = cv2.VideoCapture(0)
    # capture = cv2.VideoCapture(cv2.CAP_V4L2)
    window_name = 'Detetar faces e arestas'

    # Load the detector
    detector = dlib.get_frontal_face_detector()

    while True:
        # Capture the video frame
        _, frame = capture.read()

        # Grayscaling image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Blur the image for better edge detection
        img_blur = cv2.GaussianBlur(gray, (3, 3), 0)

        # Take the size of the frame
        height,width,_ = frame.shape

        # Create a copy to preserve the original image
        image_gui = copy.deepcopy(frame)

        # Detect faces
        #faces = faceCascade.detectMultiScale(img_blur, 1.1, 4)
        faces = detector(img_blur)

        # Canny Edge Detection
        edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
        edges_mask = edges.astype(bool)

        # Draw the rectangle around each face
        for face in faces:
            x1 = face.left()  # left point
            y1 = face.top()  # top point
            x2 = face.right()  # right point
            y2 = face.bottom()  # bottom point
            cv2.rectangle(image_gui, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw a rectangle where a face is detected

            mask_face = np.ndarray((height,width), dtype=np.uint8) # create a mask same size as image
            mask_face.fill(0) # set image to all zeros
            mask_face = cv2.rectangle(mask_face, (x, y), (x+w, y+h), 255, -1) # draw blue rectangle around face

            edges_mask[y:y + h, x:x + w] = False   # do not detect edges on face

            cv2.add(frame, (-10, 50, -10, 0), dst = image_gui, mask = mask_face) # paint face color green


        # Paint red the edges
        image_gui[edges_mask] = (0,0,255)

        # Display
        cv2.imshow(window_name, image_gui)

        # Exit the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # After the loop release the cap object
    capture.release()

    # Destroy all the windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()