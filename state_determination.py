#!/usr/bin/env python
import rospy
import sys
import os
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import Bool

class ImageListener:
	def __init__(self):
		rospy.init_node('state_node', anonymous=True)

		self.image_sub = rospy.Subscriber("/camera/depth/image_rect_raw", Image, self.imageDepthCallback)
		self.state_pub = rospy.Publisher("/state", Bool, queue_size=1)
		
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

		print(self.center)
		#Assume: velocity is constant and slow
		#isolate middle 5 values, 45 deg left, 45 deg right
		#average each

		#true = 1 = hallway, false = 2 = turn
		if self.center/1000 > 2 and (self.right - self.left) < 20:
			self.state_pub.publish(True)
		else:
			self.state_pub.publish(False)

if __name__ == '__main__':
    ImageListener()
	rospy.spin()