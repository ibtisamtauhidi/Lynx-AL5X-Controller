#!/usr/bin/env python
import rospy
import math
from sensor_msgs.msg import JointState
#import serial
#ser = serial.Serial('/dev/ttyACM0',9600)

p_deg=[0.,0.,0.,0.]

def callback(data):
    global p_deg, ser
    val = data.position
    deg = []
    for i in range(len(val)):
	deg.append(int(round(math.degrees(val[i]))))
    
    '''
    if p_deg[0] != deg[0]:
	ser.write(str(deg[0])+"w")
    if p_deg[1] != deg[1]:
	ser.write(str(deg[1])+"x")
    if p_deg[2] != deg[2]:
	ser.write(str(deg[2])+"y")
    if p_deg[3] != deg[3]:
	ser.write(str(deg[3])+"z")
    '''
    print(deg)
    p_deg = deg
    
def listener():
    rospy.init_node('snx_rad2deg', anonymous=True)
    rospy.Subscriber("joint_states", JointState, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
