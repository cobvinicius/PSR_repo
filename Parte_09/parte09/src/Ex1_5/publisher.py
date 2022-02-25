#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from parte09.msg import Dog
import colorama

# Ex5 -> roslaunch parte09_bringup bringup.launch

def main():
    # ---------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------

    rospy.init_node('publisher', anonymous=True)
    pub = rospy.Publisher('topic', Dog, queue_size=10)

    # read private parameter
    frequency = rospy.get_param("~frequency", default=10) #rosparam set /my_publisher/frequency VALUE  (obs-> my_publisher is the node name)

    rate = rospy.Rate(frequency)  # 10hz


    # ---------------------------------------------------
    # Execution
    # ---------------------------------------------------
    while not rospy.is_shutdown():
        # read global parameter
        highlight_text_color = rospy.get_param("/highlight_text_color")  # rosparam set highlight... color

        # create a dog message to send
        dog = Dog()
        dog.name = 'boby'
        dog.age = 2
        dog.color = 'brown'
        dog.brothers.append('rosita')
        dog.brothers.append('max')

        rospy.loginfo('Sending Dog ... ' +
                    getattr(colorama.Fore, highlight_text_color) + str(dog.name) +
                    colorama.Style.RESET_ALL)
        pub.publish(dog)
        rate.sleep()

    # ---------------------------------------------------
    # Termination
    # ---------------------------------------------------


if __name__ == '__main__':
    main()


