#!/usr/bin/env python3.6

import sys
sys.path.append("/Users/ab17362/OneDrive - University of Bristol/Python_modules")
from my_module import *

import pygame
from pygame.sprite import Sprite
from random import randint
from pygame.sprite import Group

def run_game():
    """runs game"""

    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Ball dropper")

    ship = Ship(settings, screen)
    balls = Group()
    create_ball(settings, screen, balls)

    while True:
        check_for_events(settings, screen, ship)
        ship.update()

        for ball in balls.sprites():
            ball.update()
            check_collision(settings, screen, ship, ball, balls)
        #if ball:
            #ball.update()
        #else:
            #initialise_ball(settings, screen)

        update_screen(settings, screen, ship, ball)

class Ship(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("ship1.bmp")
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.width/2
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        #Movement flag
        self.left_down = False
        self.right_down = False
        self.a_down = False
        self.d_down = False


    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.right_down or self.d_down and self.rect.right < self.screen_rect.right:
            self.center = min(self.center + self.settings.ship_speed_factor, self.screen_rect.right - (self.rect.right-self.rect.left)/2)
        if self.left_down or self.a_down and self.rect.left > 0:
            self.center = max(self.center - self.settings.ship_speed_factor, (self.rect.right-self.rect.left)/2)
        # Update rect object from self.center.
        self.rect.centerx = self.center


class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (20, 20, 80)

        self.ship_speed_factor = 8.5

class Ball(Sprite):
    def __init__(self, settings, screen):
        super().__init__()
        self.screen = screen
        self.settings = settings

        #image and rectangle
        self.image = pygame.image.load("Raindrop.bmp")
        self.rect = self.image.get_rect()

        #Start each new ed at the top left of the screen
        self.rect.centerx = randint(0, screen.get_rect().width)
        self.rect.y = 0

        #store the position
        self.y = float(self.rect.y)


    def blitme(self):
        """draw the ed at it's current position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += 15
        self.rect.y = self.y

#def initialise_ball(settings, screen):
#    ball = Ball(settings, screen)


def check_for_events(settings, screen, ship):
    """respond to user input"""

    #watch for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #quit
            sys.exit()

        #if a key is pressed
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ship)
        #if a key is released
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, settings, screen, ship):
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
    #if q
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """look for keyUP events to set the flags"""
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

def update_screen(settings, screen, ship, ball):
    """update the images on the screen and flip"""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_colour)
    ship.blitme()
    ball.blitme()
    #Make the last frame visable
    pygame.display.flip()

def check_collision(settings, screen, ship, ball, balls):
    collisions = pygame.sprite.collide_rect(ship, ball)
    ground = False
    if ball.rect.bottom >= screen.get_rect().bottom:
        ground = True

    if collisions or ground:
        balls.remove(ball)
        create_ball(settings, screen, balls)

def create_ball(settings, screen, balls):
    """create an ed to add to the screen"""
    ball = Ball(settings, screen)
    balls.add(ball)


run_game()
