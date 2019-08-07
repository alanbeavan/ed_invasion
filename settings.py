#!/usr/bin/env python3.6

import sys
sys.path.append("/Users/ab17362/OneDrive - University of Bristol/Python_modules")
from my_module import *

class Settings():
    """all the things that are likely to change during the development of the program"""

    def __init__(self):
        #Speed factor
        speed_factor = 5
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (20, 20, 80)

        #ship settings
        self.ship_speed_factor = 9 * speed_factor
        self.ship_limit = 3 

        # Bullet settings
        self.bullet_speed_factor = 13 * speed_factor
        self.bullet_width = 3 
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.bullets_allowed = 8

        #ed settings
        self.ed_speed_factor = 10 *speed_factor
        self.ed_descend_factor = 15 *speed_factor
        self.ed_direction_flag = 1
