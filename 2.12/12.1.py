#!/usr/bin/env python3.6

#ed_invasion.py
#make a game which is basically space invaders but instead of aliens its eds.

#Importing my personal module
import sys
sys.path.append("/Users/ab17362/OneDrive - University of Bristol/Python_modules")
from my_module import *

#importing other modules
import pygame

def run_game():
    """Creates a window in which the game is played"""

    pygame.init()

    #initialise settings
    screen_width = 1200
    screen_height = 800
    bg_colour = (0, 0, 255)

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("2.12")

    while True:
        #watch for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #quit
                sys.exit()

        screen.fill(bg_colour)
        
        #Make the last frame visable
        pygame.display.flip()

run_game()
