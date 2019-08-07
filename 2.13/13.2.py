#!/usr/bin/env python3.6

import sys
sys.path.append("/Users/ab17362/OneDrive - University of Bristol/Python_modules")
from my_module import *
import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from random import randint

class Settings():
    """all the things that are likely to change during the development of the program"""

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (16, 16, 16)

class Star(Sprite):
    """A class to represent the star"""

    def __init__(self, settings, screen):
        """initialise one ed in starting position"""
        super().__init__()
        self.screen = screen
        self.settings = settings

        #image and rectangle
        self.image = pygame.image.load("proxima-centauri.bmp")
        self.rect = self.image.get_rect()

        #Start each new ed at the top left of the screen
        self.rect.x = self.rect.width/2
        self.rect.y = self.rect.height/2


    def blitme(self):
        """draw the ed at it's current position"""
        self.screen.blit(self.image, self.rect)

def get_n_cols(settings, width):
    """get the number of eds in 1 row"""
    available_space_x = settings.screen_width
    number_cols = int(available_space_x / (1.1 * width) + 1)
    return number_cols

def get_n_rows(settings, height):
    """find the number of rows of eds to give the player a chance"""
    available_space_y = settings.screen_height
    nrows = int(available_space_y/(1.1*height) + 1)
    return nrows

def create_star(settings, screen, stars, col_n, row_n):
    """create an ed to add to the screen"""
    star = Star(settings, screen)
    width = star.rect.width
    height = star.rect.height
    star.x = randint(0, settings.screen_width)
    star.y = randint(0, settings.screen_height)
    star.rect.x = star.x
    star.rect.y = star.y
    stars.add(star)

def create_stars(settings, screen, stars):
    """create a full grid of stars"""
    star = Star(settings, screen)
    number_stars_x = get_n_cols(settings, star.rect.width)
    number_stars_y = get_n_rows(settings, star.rect.height)
    #create first row of stars
    for i in range(number_stars_y):
        for j in range(number_stars_x):
            create_star(settings, screen, stars, j, i)

def main():
    """makes a grid of stars"""
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("stars oooo")

    stars = Group()
    create_stars(settings, screen, stars)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()


        # Redraw the screen during each pass through the loop.
        screen.fill(settings.bg_colour)
        stars.draw(screen)

        #Make the last frame visable
        pygame.display.flip()
main()
