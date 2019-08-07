#!/usr/bin/env python3.6

import sys
sys.path.append("/Users/ab17362/OneDrive - University of Bristol/Python_modules")
from my_module import *

import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

class Raindrop(Sprite):
    """A class to represent the enemy"""

    def __init__(self, settings, screen):
        """initialise one ed in starting position"""
        super().__init__()
        self.screen = screen
        self.settings = settings

        #image and rectangle
        self.image = pygame.image.load("Raindrop.bmp")
        self.rect = self.image.get_rect()

        #Start each new ed at the top left of the screen
        self.rect.x = 0
        self.rect.y = 0

        #store the position
        self.x = float(self.rect.x)

    def blitme(self):
        """draw the ed at it's current position"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """update the position of the eds"""

        self.y += 25
        self.rect.y = self.y

class Settings():
    """all the things that are likely to change during the development of the program"""

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (20, 20, 20)

def create_drop(settings, screen, rain, col_n):
    """create an ed to add to the screen"""
    drop = Raindrop(settings, screen)
    drop_width = drop.rect.width
    drop_height = drop.rect.height
    drop.x = 1.5 * drop_width * col_n
    drop.y = (drop_height/2)
    drop.rect.x = drop.x
    drop.rect.y = drop.y
    rain.add(drop)

def create_rain(settings, screen, rain):
    """create a full fleet of eds"""
    drop = Raindrop(settings, screen)
    num_cols = get_n_cols(settings, drop.rect.width)

    #create first row of rain
    for j in range(num_cols):
        create_drop(settings, screen, rain, j)

def get_n_cols(settings, width):
    """get the number of drops in 1 row"""
    available_space_x = settings.screen_width
    number_drops_x = int(available_space_x / (1.5 * width)+1)
    return number_drops_x

def check_floor(settings, rain, screen):
    for drop in rain.sprites():
        screen_rect = screen.get_rect()
        if drop.rect.y >= screen_rect.bottom:
            rain.remove(drop)
        if rain:
            continue
        else:
            create_rain(settings, screen, rain)

def main():
    """make window for the rain"""
    pygame.init()

    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Rain")

    rain = Group()
    create_rain(settings, screen, rain)
    rain.draw(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

        screen.fill(settings.bg_colour)
        rain.draw(screen)
        rain.update()
        check_floor(settings, rain, screen)
        pygame.display.flip()

main()
