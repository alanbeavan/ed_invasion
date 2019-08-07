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
from ed import Ed
from game_stats import GameStats

def run_game():
    """Creates a window in which the game is played"""

    pygame.init()

    #initialise settings
    settings = Settings()


    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Ed Invasion")

    #make ship
    ship = Ship(settings, screen)
    #make a group to store bullets in
    bullets = Group()
    #make eds group and put eds in it
    eds = Group()
    gf.create_fleet(settings, screen, ship, eds)
    #initialise stats
    stats = GameStats(settings)
    game_over_flag = 0
    #While loop to kepe the game going until quit
    while True:
        #respond to user input.
        gf.check_events(settings, screen, ship, bullets)

        if stats.game_active:

            ship.update()
            gf.update_bullets(bullets, eds, settings, screen, ship)
            gf.update_eds(settings, stats, screen, ship, eds, bullets)

        elif game_over_flag == 0:
            print("Game Over...\nq to quit\n\n")
            game_over_flag = 1
        #update screen
        gf.update_screen(settings, screen, ship, eds, bullets)

run_game()
