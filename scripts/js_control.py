#!/usr/bin/env python
import rospy
import math
from lynx.msg import JoystickValues
from sensor_msgs.msg import JointState
from std_msgs.msg import Header

angles = [0.,0.,0.,0.]

def process_js(data):
	global angles
	axes = data.axes
	buttons = data.buttons
	if buttons[4] == 1 and angles[0] < math.pi:
		angles[0] += 0.03
	elif buttons[5] == 1 and angles[0] > 0.01:
		angles[0] -= 0.03
	if axes[1] == -1 and angles[1] < math.pi:
		angles[1] += 0.03
	elif axes[1] == 1 and angles[1] > 0.01:
		angles[1] -= 0.03
	elif axes[0] == -1 and angles[2] < math.pi:
		angles[2] += 0.03
	elif axes[0] == 1 and angles[2] > 0.01:
		angles[2] -= 0.03
	elif axes[3] == -1 and angles[3] < math.pi:
		angles[3] += 0.03
	elif axes[3] == 1 and angles[3] > 0.01:
		angles[3] -= 0.03

def talker():
    global angles
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rate = rospy.Rate(10)
    joint_states = JointState()
    joint_states.header = Header()
    while not rospy.is_shutdown():
    	joint_states.header.stamp = rospy.Time.now()
    	joint_states.name = ['servo1', 'servo2', 'servo3', 'servo4']
    	joint_states.position = angles
    	joint_states.velocity = []
    	joint_states.effort = []
    	pub.publish(joint_states)
	print(joint_states)
    	rate.sleep()

if __name__ == '__main__':
	rospy.init_node('joint_state_publisher')
	rospy.Subscriber("joystick_values", JoystickValues, process_js)
	talker()
