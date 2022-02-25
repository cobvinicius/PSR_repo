#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from parte09.msg import Dog


# ./listener.py

def callbackMsgReceived(msg):
    rospy.loginfo("Received a dog named " + msg.name + ' which is ' + str(msg.age) + ' years old.')

def main():
    # ---------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------

    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('topic', Dog, callbackMsgReceived)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    main()