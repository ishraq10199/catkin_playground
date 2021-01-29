execute_process(COMMAND "/home/i_ssh_rq/catkin_ws/build/imu_parser/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/i_ssh_rq/catkin_ws/build/imu_parser/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
