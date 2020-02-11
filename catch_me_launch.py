import pygame
from pygame.sprite import Group

import game_functions as gf
from character import Character
from mushroom import Mushroom
from settings import Settings


def run_game():
    pygame.init()
    ai_settings = Settings(pygame.image.load('Mushroom.png'))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    character = Character(ai_settings, screen)
    mushroom = Mushroom(ai_settings, screen)

    gf.set_random_coords_mushroom(mushroom, ai_settings.screen_width, ai_settings.screen_height)
    mushrooms = Group(mushroom)

    while True:
        gf.check_events(ai_settings, screen, character)
        character.update()
        gf.update_screen(ai_settings, screen, character, mushrooms)
        gf.update_mushrooms(mushrooms)

        deleted_count = gf.remove_mushrooms_collided(character, mushrooms)
        if deleted_count != 0:
            gf.crete_new_mushrooms(mushrooms, ai_settings, screen)

run_game()