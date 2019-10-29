#!/usr/bin/env python
import rospy
# subscribe msg to float32
from racecar_simulator.msg import Twist_float
# publish msg driving messages
from ackermann_msgs.msg import AckermannDriveStamped

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
    def __init__(self, sub_topic_name = '/twist_float'):
        # publisher
        self._drive_publisher = rospy.Publisher('/drive', AckermannDriveStamped, queue_size=1)
        # subscriber
        self._sub_topic_name = sub_topic_name
        self._twist_subscriber = rospy.Subscriber( self._sub_topic_name, Twist_float, self.topic_callback)

        # get message
        self._drive_msg = AckermannDriveStamped()
        self._twist_msg = Twist_float()


    def topic_callback(self, msg):
        self._twist_msg = msg
        rospy.loginfo(self._twist_msg)


        self.pub_drive(self._twist_msg)



    def get_angle(self):
        '''
        returns newewst angle data

        float32 data

        '''

        return self._angle_msg


    def pub_drive(self, msg):

        self._drive_msg.drive.steering_angle = msg.angle

        self._drive_msg.drive.speed = msg.vel

        self._drive_publisher.publish(self._drive_msg)



if __name__ == '__main__':
    rospy.init_node('cmd_vel_node' , log_level=rospy.INFO)
    publish_driving()
    rospy.spin()



