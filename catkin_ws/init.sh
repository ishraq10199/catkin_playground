#!/bin/bash

source ~/catkin_ws/devel/setup.bash
cd ~/catkin_ws/
catkin_make
rospack profile
