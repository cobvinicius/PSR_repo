#!/usr/bin/python3

import copy
import cv2
import numpy as np
import audioop
import colorama
import pyaudio
import wave

def main():

    # Initialize the parameters for sound detect code
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    # Get sound
    sound = pyaudio.PyAudio()
    stream = sound.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)

    # Initialize the cascade:
    faceCascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

    # initial setup
    capture = cv2.VideoCapture(0)
    window_name = 'Detetar faces e arestas'

    while True:

        # Capture the video frame
        ret, frame = capture.read()

        # Grayscaling image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Blur the image for better edge detection
        img_blur = cv2.GaussianBlur(gray, (3, 3), 0)

        # Take the size of the frame
        height,width,_ = frame.shape

        # Create a copy to preserve the original image
        image_gui = copy.deepcopy(frame)

        # Detect faces
        faces = faceCascade.detectMultiScale(img_blur, 1.1, 4)

        # Canny Edge Detection
        edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)
        edges_mask = edges.astype(bool)

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(image_gui, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw a rectangle where a face is detected

            mask_face = np.ndarray((height,width), dtype=np.uint8) # create a mask same size as image
            mask_face.fill(0) # set image to all zeros
            mask_face = cv2.rectangle(mask_face, (x, y), (x+w, y+h), 255, -1) # draw blue rectangle around face

            edges_mask[y:y + h, x:x + w] = False   # do not detect edges on face

            cv2.add(frame, (-10, 50, -10, 0), dst = image_gui, mask = mask_face) # paint face color green

            # Speak detection
            data = stream.read(CHUNK)
            rms = audioop.rms(data, 2)

            print(str(rms))

            if rms > 1500:
                text = 'Vinicius esta falando merda'
                cv2.putText(image_gui, text, (x+w, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2) # , cv2.LINE_AA, False
            else:
                text = 'Vinicius esta quietinho'
                cv2.putText(image_gui, text, (x + w, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2) #


        # Paint red the edges
        image_gui[edges_mask] = (0,0,255)

        # Display
        cv2.imshow(window_name, image_gui)

        # Exit the program
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # After the loop release the cap object
    capture.release()

    # Termination (sound part)
    stream.stop_stream()
    stream.close()
    sound.terminate()

    # Destroy all the windows
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()