import sys
from random import randint

import pygame


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



def prepare_mushroom(mushroom, mushroom_number, row_number):
    mushroom_width = mushroom.rect.width
    mushroom.rect.x = mushroom_width + 2 * mushroom_width * mushroom_number
    mushroom.rect.y = mushroom.rect.height + 2 * mushroom.rect.height * row_number

    random_factor = 40
    mushroom.rect.x += randint(-random_factor, random_factor)
    mushroom.rect.y += randint(-random_factor, random_factor)


def update_mushrooms(mushrooms, character):
    for o in mushrooms:
        o.update()
        remove_out_of_screen_mushrooms(o)

    collisions = pygame.sprite.spritecollide(character, mushrooms, True)


def remove_out_of_screen_mushrooms(mushroom):
    if mushroom.check_bottom():
        mushroom.remove()

def update_screen(ai_settings, screen, charater, mushrooms):
    screen.fill(ai_settings.bg_color)
    charater.blitme()
    for o in mushrooms:
        o.blitme()
    pygame.display.flip()