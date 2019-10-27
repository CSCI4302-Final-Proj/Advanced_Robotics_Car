#!/usr/bin/env python
import rospy
import sys
import os
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import Bool

def imageDepthCallback(self, data):
    try:
        cv_image = self.bridge.imgmsg_to_cv2(data, data.encoding)
        pix = (data.width/2, data.height/2)
        sys.stdout.write('%s: Depth at center(%d, %d): %f(mm)\r' % (self.topic, pix[0], pix[1], cv_image[pix[1], pix[0]]))
        self.center = cv_image[pix[1], pix[0]]
        self.right = cv_image[data.width, pix[1]]
        self.left = cv_image[0, pix[1]]
        sys.stdout.flush()
    except CvBridgeError as e:
        print(e)
        return
    
def listener():
	def __init__(self):
    	rospy.init_node('state', anonymous=True)

    	rospy.Subscriber("/camera/depth/image_rect_raw", Image, callback)
    	state_pub = rospy.Publisher("/state", Bool, queue_size=1)

    	# spin() simply keeps python from exiting until this node is stopped

    	print self.center
    	#Assume: velocity is constant and slow
    	#isolate middle 5 values, 45 deg left, 45 deg right
    	#average each

    	while not rospy.is_shutdown(): #true = 1 = hallway, false = 2 = turn
    		if self.center/1000 > 2 and (self.right - self.left) < 20:
	    		state_pub.publish(True)
	    	else:
	    		state_pub.publish(False)

    	rospy.spin()

if __name__ == '__main__':
    listener()