#!/usr/bin/env python
import rospy
import numpy as np
import math
from mavros_msgs.msg import PositionTarget
from geometry_msgs.msg import PoseStamped, TwistStamped
from sensor_msgs.msg import LaserScan
import time


regions = {
    'right': 0,
    'fright': 0,
    'front': 0,
}

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

inf = 10

def clbk_laser(msg):
   global regions, inf
    # Determination of minimum distances in each region
   regions = {
      'fright':  min(mean(msg.ranges[0:90]), inf),
      'front':  min(mean(msg.ranges[140:220]), inf),
      'fleft':   min(mean(msg.ranges[260:359]), inf),
   
    }
   
   # if (regions['front']<=0.04):
   #    set_velocity.twist.linear.x = 0
   #    set_velocity.twist.angular.z = 0.4
   #    time.sleep(1)
   # else:
   #    set_velocity.twist.linear.x = -1
   #    set_velocity.twist.angular.z = 0



rospy.init_node('Vel_Control_Node', anonymous = True)
rate = rospy.Rate(10) #publish at 10 Hz

distance = rospy.Subscriber('/scan', LaserScan, clbk_laser)

while not rospy.is_shutdown():
  
   rate.sleep()
