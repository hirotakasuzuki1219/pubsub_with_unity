#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from pubsub_unity_test.msg import MyMsg
from datetime import datetime

rospy.init_node('pub')
pub = rospy.Publisher('UnixTime', MyMsg , queue_size=1)
mymsg_unity = MyMsg()

rate = rospy.Rate(10)
while not rospy.is_shutdown():
    mymsg_unity.MsgWithUnity = 1
    # now = rospy.get_time()
    pub.publish(mymsg_unity)
    rate.sleep()

