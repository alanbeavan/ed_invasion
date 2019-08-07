#!/usr/bin/env python3.6

import sys
sys.path.append("/Users/ab17362/OneDrive - University of Bristol/Python_modules")
from my_module import *
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """creates a class for bullet on which the things can happen"""

    def __init__(self, settings, screen, ship):
        """initialises bullet with the things we need"""
        #inherit from Sprite
        super().__init__()

        #work with the screen we have
        self.screen = screen

        #create a bullet at 0,0
        self.rect = pygame.Rect(0,0, settings.bullet_width, settings.bullet_height)
        #move it
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #store the y position of the bullet as a decimal value
        self.y = float(self.rect.y)

        #aesthetics of the bullet
        self.colour = settings.bullet_colour
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """move the bullet to the top of the screen"""
        #update y value
        self.y -= self.speed_factor
        #update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet to the screen"""
        pygame.draw.rect(self.screen, self.colour, self.rect)
