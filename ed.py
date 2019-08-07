#!/usr/bin/env python3.6

import sys
sys.path.append("/Users/ab17362/OneDrive - University of Bristol/Python_modules")
from my_module import *

import pygame
from pygame.sprite import Sprite

class Ed(Sprite):
    """A class to represent the enemy"""

    def __init__(self, settings, screen):
        """initialise one ed in starting position"""
        super().__init__()
        self.screen = screen
        self.settings = settings

        #image and rectangle
        self.image = pygame.image.load("images/ed.bmp")
        self.rect = self.image.get_rect()

        #Start each new ed at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height/2 - 30

        #store the position
        self.x = float(self.rect.x)

    def blitme(self):
        """draw the ed at it's current position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """update the position of the eds"""
        self.x += self.settings.ed_speed_factor * self.settings.ed_direction_flag
        self.rect.x = self.x

    def check_collisions(self):
        """change directions if the eds hit the edge of the screen
        return True if it does"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
