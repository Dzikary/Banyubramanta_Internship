# http://ros.org/doc/groovy/api/catkin/html/user_guide/supposed.html
cmake_minimum_required(VERSION 2.8.3)
project(joy)

#anita
if(NOT WIN32)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wno-narrowing -Wall -Wdeprecated-declarations")
#  set(CEF_C_COMPILER_FLAGS  -Wno-narrowing)
endif()

set(ROS_BUILD_TYPE Debug)

##############
## Packages ##
##############

### ROS 1 ###

# Load catkin and all dependencies required for this package
#set(CATKIN_DEPS roscpp diagnostic_updater sensor_msgs)
#set(ROSDEP_DEPS joystick)
#find_package(catkin REQUIRED ${CATKIN_DEPS})
#catkin_package(DEPENDS ${CATKIN_DEPS} ${ROSDEP_DEPS})

### ROS 2 ###

set(AMENT_DEPS rclcpp diagnostic_updater sensor_msgs)
set(ROSDEP_DEPS joystick)
find_package(ament_cmake REQUIRED ${AMENT_DEPS})
#ament_package(DEPENDS ${AMENT_DEPS} ${ROSDEP_DEPS})

find_package(rmw REQUIRED)#ROS Middleware (rmw) Interface
find_package(rmw_implementation REQUIRED)#CMake infrastructure and dependencies for rmw implementations


###################################
## ament specific configuration ##
###################################

if(AMENT_ENABLE_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()

set(target_dependencies
  "rclcpp"
  "sensor_msgs"
  "diagnostic_updater")

###########
## Build ##
###########

### ROS 1 ###

#include(CheckIncludeFiles)
#check_include_files(linux/joystick.h HAVE_LINUX_JOYSTICK_H)

#if(HAVE_LINUX_JOYSTICK_H)
#  include_directories(msg/cpp ${catkin_INCLUDE_DIRS})
#  add_executable(joy_node src/joy_node.cpp)
#  target_link_libraries(joy_node ${catkin_LIBRARIES})
#else(HAVE_LINUX_JOYSTICK_H)
#  message("Warning: no <linux/joystick.h>; won't build joy node")
#endif(HAVE_LINUX_JOYSTICK_H)

#catkin_add_nosetests(test/test_joy_msg_migration.py)

# Install targets
#install(TARGETS joy_node
#  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

#install(DIRECTORY migration_rules
#  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
#  )


### ROS 2 ###

# Look for <linux/joystick.h>
include(CheckIncludeFiles)
check_include_files(linux/joystick.h HAVE_LINUX_JOYSTICK_H)

if(HAVE_LINUX_JOYSTICK_H)
  include_directories(msg/cpp ${ament_INCLUDE_DIRS})
  add_executable_for_each_rmw_implementations(joy_node 
  src/joy_node.cpp
  TARGET_DEPENDENCIES ${target_dependencies} INSTALL)
  
else(HAVE_LINUX_JOYSTICK_H)
  message("Warning: no <linux/joystick.h>; won't build joy node")
endif(HAVE_LINUX_JOYSTICK_H)

#catkin_add_nosetests(test/test_joy_msg_migration.py)

# Install targets
install(TARGETS joy_node
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION lib/${PROJECT_NAME})

install(DIRECTORY migration_rules
  DESTINATION share/${PROJECT_NAME}
  )

