#!/usr/bin/env python3.6

import sys
sys.path.append("/Users/ab17362/OneDrive - University of Bristol/Python_modules")
from my_module import *
import pygame

def run_game():
    """print the key to the terminal when pressed"""
    pygame.init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #quit
                sys.exit()

            if event.type == pygame.KEYDOWN:
                print(event.key)

run_game()
