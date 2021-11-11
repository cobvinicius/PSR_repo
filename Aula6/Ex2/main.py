#!/usr/bin/python3

import cv2

def main():
    # initial setup
    capture = cv2.VideoCapture(0)
    window_name = 'Detetar imagem'

    # Using a video instead
    # capture = cv2.VideoCapture('test.mp4') # need to be in the same directory

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