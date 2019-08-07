#!/usr/bin/env python3.6

#ed_invasion.py
#make a game which is basically space invaders but instead of aliens its eds.

#Importing my personal module
import sys
sys.path.append("/Users/ab17362/OneDrive - University of Bristol/Python_modules")
from my_module import *

#importing other modules
import pygame

class Sprite():
    """class of the player controlled ship"""

    def __init__(self, screen):
        """initialise the ship and set it's starting posision"""
        self.screen = screen

        #load in the image of the ship and get it's rectangle
        self.image = pygame.image.load('to_use.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #The ship starts at the centre of the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery


    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)


def run_game():
    """Creates a window in which the game is played"""

    pygame.init()

    #initialise settings
    screen_width = 1200
    screen_height = 800
    bg_colour = (0, 0, 255)

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("2.12")

    beetle = Sprite(screen)

    while True:
        #watch for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #quit
                sys.exit()

        screen.fill(bg_colour)
        beetle.blitme()

        #Make the last frame visable
        pygame.display.flip()

run_game()
