#!/usr/bin/env python3.6

import sys
sys.path.append("/Users/ab17362/OneDrive - University of Bristol/Python_modules")
from my_module import *
import pygame
from bullet import Bullet
from ed import Ed
from time import sleep

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

def get_n_eds_x(settings, width):
    """get the number of eds in 1 row"""
    available_space_x = settings.screen_width - 2 * width
    number_eds_x = int(available_space_x / (1.5 * width))
    return number_eds_x

def get_n_rows(settings, ship_height, ed_height):
    """find the number of rows of eds to give the player a chance"""
    available_space_y = settings.screen_height - ed_height/2 - 30 - ship_height * 3
    nrows = int(available_space_y/(1.2*ed_height))
    return nrows


def create_ed(settings, screen, eds, col_n, row_n):
    """create an ed to add to the screen"""
    ed = Ed(settings, screen)
    ed_width = ed.rect.width
    ed_height = ed.rect.height
    ed.x = ed_width + 1.5 * ed_width * col_n
    ed.y = (ed_height/2-30) + 1.2 * ed_height * row_n
    ed.rect.x = ed.x
    ed.rect.y = ed.y
    eds.add(ed)

def create_fleet(settings, screen, ship, eds):
    """create a full fleet of eds"""
    ed = Ed(settings, screen)
    number_eds_x = get_n_eds_x(settings, ed.rect.width)
    number_eds_y = get_n_rows(settings, ship.rect.height, ed.rect.height)
    #create first row of eds
    for i in range(number_eds_y):
        for j in range(number_eds_x):
            create_ed(settings, screen, eds, j, i)

def check_keydown_events(event, settings, screen, ship, bullets):
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
    #if the event is spacebar
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, screen, ship, bullets)
    #if q
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(settings, screen, ship, bullets):
    """Create a new bullet and add it to the bullets group. Position it correctly"""
    if len(bullets) < settings.bullets_allowed:
        bullet = Bullet(settings, screen, ship)
        bullets.add(bullet)

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


def update_screen(settings, screen, ship, eds, bullets):
    """update the images on the screen and flip"""
    # Redraw the screen during each pass through the loop.
    screen.fill(settings.bg_colour)
    ship.blitme()
    eds.draw(screen)
    #redraw all bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    #Make the last frame visable
    pygame.display.flip()


def update_bullets(bullets, eds, settings, screen, ship):
    """updates bullets"""

    bullets.update()

    #get rid of bullets at the top of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets, eds, True, True)

    if len(eds) == 0:
        bullets.empty()
        create_fleet(settings, screen, ship, eds)

def check_bullet_ed_collision(settings, screen, ship, eds, bullets):
    """remove bullet and ed if collision"""
    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets, eds, True, True)

    if len(eds) == 0:
        bullets.empty()
        create_fleet(settings, screen, ship, eds)


def update_eds(settings, stats, screen, ship, eds, bullets):
    """update the position of the eds after checking if they are at the edge"""
    check_fleet_edges(settings, eds)
    eds.update()

    #look for collisions with the ship
    if pygame.sprite.spritecollideany(ship, eds):
        ship_hit(settings, stats, screen, ship, eds, bullets)

    #see if ed has hit rock bottom
    check_eds_bottom(settings, stats, screen, ship, eds, bullets)


def check_fleet_edges(settings, eds):
    """Check if the edge is hit and change directions if possible"""
    for ed in eds.sprites():
        if ed.check_collisions():
            change_direction(settings, eds)
            break

def change_direction(settings, eds):
    """drop the eds and change direction"""
    for ed in eds.sprites():
        ed.rect.y += settings.ed_descend_factor
    settings.ed_direction_flag *= -1

def ship_hit(settings, stats, screen, ship, eds, bullets):
    """respond to the ship being hit"""
    #decrement ships left
    if stats.ships_left > 0:
        stats.ships_left -= 1
        #remove eds and bullets
        bullets.empty()
        eds.empty()

        #recreate the fleet and reset the ship's position
        create_fleet(settings, screen, ship, eds)
        ship.center_ship()

        #wait
        sleep(0.5)
    else:
        stats.game_active = False


def check_eds_bottom(settings, stats, screen, ship, eds, bullets):
    """check if any eds have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for ed in eds.sprites():
        if ed.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, screen, ship, eds, bullets)
            break
