#!/usr/bin/env python3.6

#ed_invasion.py
#make a game which is basically space invaders but instead of aliens its eds.

#Importing my personal module
import sys
sys.path.append("/Users/ab17362/OneDrive - University of Bristol/Python_modules")
from my_module import *

#importing other modules
import pygame
from settings import *
from ship import *
import game_functions as gf
from pygame.sprite import Group

def run_game():
    """Creates a window in which the game is played"""

    pygame.init()

    #initialise settings
    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("12.5")

    #make ship
    ship = Ship(settings, screen)
    #make a group to store bullets in
    bullets = Group()

    #While loop to kepe the game going until quit
    while True:
        #respond to user input.
        gf.check_events(settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets, screen)

        #update screen
        gf.update_screen(settings, screen, ship, bullets)

run_game()
