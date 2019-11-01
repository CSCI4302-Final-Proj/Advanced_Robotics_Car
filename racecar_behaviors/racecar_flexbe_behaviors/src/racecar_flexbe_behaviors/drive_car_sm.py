#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from racecar_flexbe_states.drive_forward import GoFowardState
from racecar_flexbe_states.turn_state import TurnState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu Oct 31 2019
@author: Earl
'''
class DriveCarSM(Behavior):
	'''
	It enables us to drive the car
	'''


	def __init__(self):
		super(DriveCarSM, self).__init__()
		self.name = 'Drive Car'

		# parameters of this behavior
		self.add_parameter('my_speed', 0.4)
		self.add_parameter('my_travel_dist', 20)
		self.add_parameter('my_obstacle_dist', 1)
		self.add_parameter('my_t_speed', 0.1)
		self.add_parameter('my_turn_angle', -0.3)
		self.add_parameter('my_forward_dist', 2)
		self.add_parameter('my_timeout', 10)

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:30 y:373, x:130 y:373
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:232 y:191
			OperatableStateMachine.add('Drive Forward State',
										GoFowardState(speed=self.my_speed, travel_dist=self.my_travel_dist, obstacle_dist=self.my_obstacle_dist),
										transitions={'failed': 'failed', 'done': 'Turn State'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Off})

			# x:405 y:267
			OperatableStateMachine.add('Turn State',
										TurnState(t_speed=self.my_t_speed, turn_angle=self.my_turn_angle, forward_dist=self.my_forward_dist, timeout=self.my_timeout),
										transitions={'failed': 'failed', 'done': 'finished'},
										autonomy={'failed': Autonomy.Off, 'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
