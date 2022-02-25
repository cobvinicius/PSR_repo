#!/usr/bin/env python3
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main():

    rospy.init_node('image_publisher', anonymous=False)

    publisher = rospy.Publisher('~image', Image, queue_size=1)

    capture = cv2.VideoCapture(0)
    window_name = 'Opencv Window'
    cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

    rate = rospy.Rate(15)

    while True:
        _, image = capture.read()

        cv2.imshow(window_name, image)

        bridge = CvBridge()
        image_message = bridge.cv2_to_imgmsg(image,encoding="bgr8")
        publisher.publish(image_message)

        if cv2.waitKey(1) == ord('q'):
            break

        rate.sleep()

    capture.release()
    cv2.destroyAllWindows()


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    main()