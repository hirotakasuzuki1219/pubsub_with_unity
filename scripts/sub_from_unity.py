#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from pubsub_unity_test.msg import MyMsg
from datetime import datetime

def callback(message):
    print(message.MsgWithUnity)

if __name__ == "__main__":
    rospy.init_node('sub')
    sub = rospy.Subscriber('MsgFromUnity', MyMsg , callback)
    rospy.spin()