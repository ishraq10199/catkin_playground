#!/usr/bin/env python
import rospy
from std_msgs.msg import Header
from sensor_msgs.msg import Imu 
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Vector3

from time import sleep
import serial
ser = serial.Serial('/dev/ttyUSB1', 57600)

# Initialize the ros node
rospy.init_node('publisher_node', anonymous=True)

my_seq = 0

# Create a publisher
publisher = rospy.Publisher("/imu", Imu, queue_size=0)
rate = rospy.Rate(60)

imu_msg = Imu()
imu_msg.header.frame_id = "imu"

# TODO: Implement try catch block

while not rospy.is_shutdown():
    data = ser.readline()
    data_split = data.split()
    if(len(data_split) >= 10):
        # Prepare the data
        imu_msg.header = Header()
        my_seq = my_seq + 1
        imu_msg.header.seq = my_seq
        imu_msg.header.stamp = rospy.Time.now()
        
        imu_msg.orientation = Quaternion()
        
        imu_msg.orientation.x = float(data_split[0])
        imu_msg.orientation.y = float(data_split[1])
        imu_msg.orientation.z = float(data_split[2])
        imu_msg.orientation.w = float(data_split[3])

        imu_msg.angular_velocity = Vector3()

        imu_msg.angular_velocity.x = float(data_split[4])
        imu_msg.angular_velocity.y = float(data_split[5])
        imu_msg.angular_velocity.z = float(data_split[6])

        imu_msg.linear_acceleration = Vector3()

        imu_msg.linear_acceleration.x = float(data_split[7])
        imu_msg.linear_acceleration.y = float(data_split[8])
        imu_msg.linear_acceleration.z = float(data_split[9])

    # Publish the data
    publisher.publish(imu_msg)
    log_msg = 'Published, seq number: ' + str(imu_msg.header.seq)
    rospy.loginfo(log_msg)
    rate.sleep()
    



