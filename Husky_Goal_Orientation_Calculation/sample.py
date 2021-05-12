#!/usr/bin/env python
from tf.transformations import euler_from_quaternion 
from geometry_msgs.msg import Point
from math import atan2,sqrt
import time
from tf.transformations import quaternion_from_euler

"""
This is just a sample on how to use the conversion, you may write in your desired sub and pub based on your ROS use case. 

## Sample
odom_msg = rospy.wait_for_message('/odom', Odometry)
x = odom_msg.pose.pose.position.x
y = odom_msg.pose.pose.position.y
rot_q = odom_msg.pose.pose.orientation 
(roll,pitch,theta) = euler_from_quaternion([rot_q.x, rot_q.y, rot_q.z, rot_q.w])
##
# Do your calculation here
##
publisher = rospy.Publisher("/move_base_simple/goal",PoseStamped, queue_size=10)


"""
current_x = 1.49915555732
current_y = 2.15630462218
current_z = 0

rot_x = 0.000
rot_y = 0.0
rot_z = 0.341397684122
rot_w = 0.939918943993

(roll,pitch,theta) = euler_from_quaternion([rot_x, rot_y, rot_z, rot_w])

print("orginal:",roll,pitch,theta)

goal_x = -2
goal_y = -2
inc_x = goal_x - current_x
inc_y = goal_y - current_y
angle_to_goal = atan2(inc_y, inc_x)

theta += angle_to_goal

print("adding angle delta:",roll,pitch,theta)

(x,y,z,w) = quaternion_from_euler(roll,pitch,theta)

print(x,y,z,w)

