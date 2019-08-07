#!/usr/bin/env python3.6

import sys
sys.path.append("/Users/ab17362/OneDrive - University of Bristol/Python_modules")
from my_module import *

class GameStats():
    """class to track how the player is doing"""

    def __init__(self, settings):
        """initialise statistics"""
        self.settings = settings
        self.reset_settings()
        self.game_active = True

    def reset_settings(self):
        """set all the stats to how they ought to be at the start of the game"""
        self.ships_left = self.settings.ship_limit
