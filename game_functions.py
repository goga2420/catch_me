import sys
from random import randint

import pygame

from mushroom import Mushroom


def check_keydown_events(event, ai_settings, screen, character):
    if event.key == pygame.K_RIGHT:
        character.moving_right = True
    elif event.key == pygame.K_LEFT:
        character.moving_left = True


def check_keyup_events(event, character):
    if event.key == pygame.K_RIGHT:
        character.moving_right = False
    elif event.key == pygame.K_LEFT:
        character.moving_left = False


def check_events(ai_settings, screen, character):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, character)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, character)


def set_random_coords_mushroom(mushroom, screen_width, screen_height):
    mushroom.rect.x = randint(0, screen_width - mushroom.rect.width)
    mushroom.rect.y = randint(0, screen_height - mushroom.rect.height - 100)


def update_mushrooms(mushrooms):
    for o in mushrooms:
        o.update()
        remove_out_of_screen_mushrooms(o)


def remove_out_of_screen_mushrooms(mushroom):
    if mushroom.check_bottom():
        mushroom.remove()

def update_screen(ai_settings, screen, charater, mushrooms):
    screen.fill(ai_settings.bg_color)
    charater.blitme()
    for o in mushrooms:
        o.blitme()
    pygame.display.flip()


def remove_mushrooms_collided(character, mushrooms):
    collisions = pygame.sprite.spritecollide(character, mushrooms, True)
    return len(collisions)


def crete_new_mushrooms(mushrooms, ai_settings, screen):
    m = Mushroom(ai_settings, screen)
    set_random_coords_mushroom(m, ai_settings.screen_width, ai_settings.screen_height)
    mushrooms.add(m)
