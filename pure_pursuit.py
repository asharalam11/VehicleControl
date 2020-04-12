#**********************************************
#       Self-Driving Car - Coursera
#        Created on: April 11
#         Author: Ashar Alam
#*********************************************

import numpy as np

class PP(object):
    def __init__(self,L, k_pp):
        # L : Vehicle WheelBase
        # K_PP : Pure-pursuit look-ahead gain
        self.L = L
        self.K_PP = k_pp

    def update(self, coeffs, velocity):
        eps = 0.001
        if velocity < eps:
            steering_angle = 0.0
        else:
            # Lookahead distance is proportional to velocity and proportional to lookahead gain
            Ld_x = self.K_PP * velocity
            cte = np.polyval(coeffs, Ld_x)
            sin_alpha = cte/Ld_x
            steering_angle = np.arctan((2*self.L* sin_alpha) / (self.K_PP * velocity))

        return steering_angle
