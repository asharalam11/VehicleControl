#**********************************************
#       Self-Driving Car - Coursera
#        Created on: April 13
#         Author: Ashar Alam
#*********************************************

import numpy as np

class STANLEY(object):
    def __init__(self,L, k, k_soft = 1):
        # L : Vehicle WheelBase
        # k : Gain for crosstrack error
        # k_soft : Positive softening constant
        self.L = L
        self.k = k
        self.k_soft = k_soft


    def update(self, velocity, cte, yaw_error):
        eps = 0.001
        if velocity < eps:
            steering_angle = 0.0
        else:
            heading_compensation = yaw_error
            crosstrack_compensation = np.arctan(self.k * cte / (self.k_soft + velocity))
            steering_angle = heading_compensation + crosstrack_compensation

        return steering_angle
