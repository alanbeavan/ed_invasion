#!/usr/bin/env python3.6

import sys
sys.path.append("/Users/ab17362/OneDrive - University of Bristol/Python_modules")
from my_module import *
import pygame

def check_events(ship):
    """respond to user input"""

    #watch for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #quit
            sys.exit()

        #if a key is pressed
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        #if a key is released
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship):
    """look for key down events and do the things"""
    #if the right arrow or d
    if event.key == pygame.K_RIGHT:
        ship.right_down = True
    elif event.key == pygame.K_d:
        ship.d_down = True
    #if the left arrow or a
    elif event.key == pygame.K_LEFT:
        ship.left_down = True
    elif event.key == pygame.K_a:
        ship.a_down = True
    elif event.key == pygame.K_UP:
        ship.up_down = True
    elif event.key == pygame.K_w:
        ship.w_down = True
    elif event.key == pygame.K_DOWN:
        ship.down_down = True
    elif event.key == pygame.K_s:
        ship.s_down = True

def check_keyup_events(event, ship):
    #if the key is right or d
    if event.key == pygame.K_RIGHT:
        ship.right_down = False
    elif event.key == pygame.K_d:
        ship.d_down = False
    #if the left arrow or a
    elif event.key == pygame.K_LEFT:
        ship.left_down = False
    elif event.key == pygame.K_a:
        ship.a_down = False
    elif event.key == pygame.K_UP:
        ship.up_down = False
    elif event.key == pygame.K_w:
        ship.w_down = False
    elif event.key == pygame.K_DOWN:
        ship.down_down = False
    elif event.key == pygame.K_s:
        ship.s_down = False

def update_screen(settings, screen, ship):
    """update the images on the screen and flip"""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_colour)
    ship.blitme()

    #Make the last frame visable
    pygame.display.flip()
