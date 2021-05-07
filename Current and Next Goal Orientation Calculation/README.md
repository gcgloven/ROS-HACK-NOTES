## Calucation for goal orientation
In the scenario of calculating the navigation goal with requirement of pose & orientation, pose is easily understandable. However, how do you calculate the desired orientation from next point in space?

This is mainly desgined for navigation stack on UGV, you may use it to sort the orientation out.

## Magic of atan(delta y, delta x)
The simple trick here is to calculate the change in angle on the z plane and rotate accordingly on (r,p,y) orientation.
1. conver current quaternion orientation (x,w,z,w) to euler orientation (roll,pitch,theta)
2. theta' = atan(goal_y - current_y, goal_x - current_x)
3. new_theta = theta + theta'
4. convert (roll,pitch,new_theta) to quaternion (x,y,z,w)
4. publish new GoalStamp