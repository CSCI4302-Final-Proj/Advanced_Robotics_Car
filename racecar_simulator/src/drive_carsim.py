#!/usr/bin/env python
import rospy
# subscribe msg to float32
#from racecar_simulator.msg import Twist_float
# publish msg driving messages
from sensor_msgs.msg import LaserScan
from ackermann_msgs.msg import AckermannDriveStamped
import matplotlib.pyplot as plt

'''
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
ackermann_msgs/AckermannDrive drive
  float32 steering_angle
  float32 steering_angle_velocity
  float32 speed
  float32 acceleration
  float32 jerk
'''

class publish_driving(object): # needed for python 2 , implicit in python 3
    def __init__(self):
        # publisher
        self.drive_publisher = rospy.Publisher('/drive', AckermannDriveStamped, queue_size=1)

        # subscriber
        self.scan_subscriber = rospy.Subscriber('/scan', LaserScan, self.scan_callback)
        # get message
        self.drive_msg = AckermannDriveStamped()
        #self.pub_drive()

    def scan_callback(self, data):
        self.angles = data.ranges

        self.pub_drive()

    def pub_drive(self):
        self.drive_msg.drive.steering_angle = 0 # radians?
        self.drive_msg.drive.speed = 0 #meters/second
        self.drive_publisher.publish(self.drive_msg)



if __name__ == '__main__':
    rospy.init_node('drive_carsim' , log_level=rospy.INFO)
    publish_driving()
    rospy.spin()



