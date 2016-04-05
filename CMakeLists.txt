cmake_minimum_required(VERSION 2.8.3)
project(lynx)

find_package(catkin REQUIRED COMPONENTS
   rospy
   roslaunch
   message_generation
)
add_message_files(
  FILES
  JoystickValues.msg
)
generate_messages(
  DEPENDENCIES
)
catkin_package()

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(DIRECTORY config DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
