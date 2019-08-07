#!/usr/bin/env python3.6

import sys
sys.path.append("/Users/ab17362/OneDrive - University of Bristol/Python_modules")
from my_module import *
import pygame

class Ship():
    """class of the player controlled ship"""

    def __init__(self, settings, screen):
        """initialise the ship and set it's starting posision"""
        self.screen = screen
        self.settings = settings

        #load in the image of the ship and get it's rectangle
        self.image = pygame.image.load('../images/ship1.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #The ship starts at the centre of the left of the screen
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        print("screen left " + str(self.screen_rect.left))
        print(self.rect)
        #store x value as float for non-whole number speed mods
        self.center = float(self.rect.centery)

        #Movement flag
        self.down_down = False
        self.up_down = False
        self.s_down = False
        self.w_down = False

    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """move right if moving_down == True etc"""
        #if right and not at the edge of the screes
        if self.down_down or self.s_down and self.rect.bottom < self.screen_rect.bottom:
            self.center = min(self.center + self.settings.ship_speed_factor, self.screen_rect.bottom - (self.rect.bottom-self.rect.top)/2)
        #if left - not elif so if both are pressed, it doesn't move
        if self.up_down or self.w_down and self.rect.top > 0:
            self.center = max(self.center - self.settings.ship_speed_factor, (self.rect.bottom-self.rect.top)/2)
        # Update rect object from self.center.
        self.rect.centery = self.center
