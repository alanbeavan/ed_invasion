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

        #The ship starts at the centre of the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store x value as float for non-whole number speed mods
        self.center = float(self.rect.centerx)
        self.ycenter = float(self.rect.centery)
        #Movement flag
        self.left_down = False
        self.right_down = False
        self.up_down = False
        self.down_down = False
        self.a_down = False
        self.d_down = False
        self.w_down = False
        self.s_down = False

    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """move right if moving_right == True"""
        #if right and not at the edge of the screes
        if self.right_down or self.d_down and self.rect.right < self.screen_rect.right:
            self.center = min(self.center + self.settings.ship_speed_factor, self.screen_rect.right - (self.rect.right-self.rect.left)/2)
        #if left - not elif so if both are pressed, it doesn't move
        if self.left_down or self.a_down and self.rect.left > 0:
            self.center = max(self.center - self.settings.ship_speed_factor, (self.rect.right-self.rect.left)/2)
        #if up or w
        if self.up_down or self.w_down and self.rect.bottom > 0:
            self.ycenter = max(self.ycenter - self.settings.ship_speed_factor, (self.rect.bottom-self.rect.top)/2)
        #if down or s
        if self.down_down or self.s_down and self.rect.top < self.screen_rect.bottom:
            self.ycenter = min(self.ycenter + self.settings.ship_speed_factor, self.screen_rect.bottom - (self.rect.bottom-self.rect.top)/2)
        # Update rect object from self.center.
        self.rect.centerx = self.center
        self.rect.centery = self.ycenter
