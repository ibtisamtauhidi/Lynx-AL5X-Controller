#!/usr/bin/env python
import rospy
from lynx.msg import JoystickValues
import pygame

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()

def get():
    axes = [0,0,0,0,0]
    buttons	= [0,0,0,0,0,0,0,0,0,0,0,0]
    pygame.event.pump()
    for i in range(0, j.get_numaxes()):
        axes[i] = int(round(j.get_axis(i)))
    for i in range(0, j.get_numbuttons()):
        buttons[i] = j.get_button(i)
    return [axes,buttons]

def talker(pub):
	msg = JoystickValues()
	arr = get()
	msg.axes = arr[0]
	msg.buttons = arr[1]
	rospy.loginfo(msg)
	pub.publish(msg)

if __name__ == '__main__':
	pub = rospy.Publisher('joystick_values', JoystickValues, queue_size=10)
	rospy.init_node('JoystickController', anonymous=True)
	try:
		rate = rospy.Rate(10)
		while not rospy.is_shutdown():
			talker(pub)
			rate.sleep()
	except rospy.ROSInterruptException:
		pass
