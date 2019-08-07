#!/usr/bin/env python3.6

import sys
sys.path.append("/Users/ab17362/OneDrive - University of Bristol/Python_modules")
from my_module import *
import pygame
from bullet import Bullet

def check_events(settings, screen, ship, bullets):
    """respond to user input"""

    #watch for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #quit
            sys.exit()

        #if a key is pressed
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship, bullets)
        #if a key is released
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, settings, screen, ship, bullets):
    """look for key down events and do the things"""
    #if the right arrow or d
    if event.key == pygame.K_DOWN:
        ship.down_down = True
    elif event.key == pygame.K_s:
        ship.s_down = True
    #if the left arrow or a
    elif event.key == pygame.K_UP:
        ship.up_down = True
    elif event.key == pygame.K_w:
        ship.w_down = True
    #if the event is spacebar
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)

def fire_bullet(settings, screen, ship, bullets):
    #Create a new bullet and add it to the bullets group
    if len(bullets) < settings.bullets_allowed:
        bullet = Bullet(settings, screen, ship)
        bullets.add(bullet)

def check_keyup_events(event, ship):
    #if the key is right or d
    if event.key == pygame.K_DOWN:
        ship.down_down = False
    elif event.key == pygame.K_s:
        ship.s_down = False
    #if the left arrow or a
    elif event.key == pygame.K_UP:
        ship.up_down = False
    elif event.key == pygame.K_w:
        ship.w_down = False


def update_screen(settings, screen, ship, bullets):
    """update the images on the screen and flip"""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_colour)
    ship.blitme()

    #redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #Make the last frame visable
    pygame.display.flip()


def update_bullets(bullets, screen):
    """updates bullets"""

    bullets.update()

    #get rid of bullets at the top of the screen
    for bullet in bullets.copy():
        if bullet.rect.left >= screen.get_rect().right:
            bullets.remove(bullet)
