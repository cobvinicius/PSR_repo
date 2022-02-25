#!/usr/bin/env python3

import rospy
import tf_conversions
import tf2_ros
import geometry_msgs.msg
import math


def main():
    rospy.init_node('solar_system')

    br = tf2_ros.TransformBroadcaster()
    t = geometry_msgs.msg.TransformStamped()

    # Parameters reading to use the launch file
    distance_to_parent = rospy.get_param("~distance_to_parent")
    period = rospy.get_param("~period")
    # rotation_period = rospy.get_param("~rotation_period")

    frequency = 100
    rate = rospy.Rate(frequency)
    alpha = 0

    while not rospy.is_shutdown():

        alpha += 1/period/frequency  # higher alpha = higher velocity  (or higher frequency with low alpha)
        if alpha > 2* math.pi:
            alpha = 0

        t.header.stamp = rospy.Time.now()

        # # Sun to Mercury
        # rho = 0.387
        #
        # t.header.frame_id = 'Sun'
        # t.child_frame_id = 'Mercury'
        # t.transform.translation.x = rho * math.cos(alpha)
        # t.transform.translation.y = rho * math.sin(alpha)
        # t.transform.translation.z = 0.0
        # q = tf_conversions.transformations.quaternion_from_euler(0, 0, 10*alpha)
        # t.transform.rotation.x = q[0]
        # t.transform.rotation.y = q[1]
        # t.transform.rotation.z = q[2]
        # t.transform.rotation.w = q[3]

        # Sun to Mercury
        t.header.frame_id = rospy.remap_name('parent')
        t.child_frame_id = rospy.remap_name('child')
        t.transform.translation.x = distance_to_parent * math.cos(alpha)
        t.transform.translation.y = distance_to_parent * math.sin(alpha)
        t.transform.translation.z = 0.0
        q = tf_conversions.transformations.quaternion_from_euler(0, 0, 10*alpha)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]




        # Send the transformations
        br.sendTransform(t)

        # Sleep
        rate.sleep()

    rospy.spin()

if __name__ == '__main__':
    main()