#!/usr/bin/env python
import rospy

## ${package_name}
from package_name.srv import RPY2Q,RPY2QResponse,Q2RPY,Q2RPYResponse

from tf.transformations import euler_from_quaternion 
from tf.transformations import quaternion_from_euler

def RPYtoQuaternion (req):
    
    x,y,z,w = quaternion_from_euler(req.r, req.p,req.y)
    # #rospy.loginfo("Sum of " + str(req.a) + " and " + str(req.b) + " is " + str(result))
    ls = [x,y,z,w]
    return RPY2QResponse(ls)

def QuaterniontoRPY (req):
    
    r,p,y = euler_from_quaternion([req.x, req.y,req.z,req.w])
    # #rospy.loginfo("Sum of " + str(req.a) + " and " + str(req.b) + " is " + str(result))
    ls = [r,p,y]
    return Q2RPYResponse(ls)

if __name__ == '__main__':
    rospy.init_node("rpy_q_translator")
    service = rospy.Service("RPYtoQuaternion", RPY2Q, RPYtoQuaternion)
    service = rospy.Service("QuaterniontoRPY", Q2RPY, QuaterniontoRPY)
    
    rospy.loginfo("Service server has been started")
    rospy.spin()
