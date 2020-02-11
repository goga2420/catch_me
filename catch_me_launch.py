import pygame
import sys
from pygame.sprite import Group
from game_stats import GameStats
import game_functions as gf
from character import Character
from settings import Settings


def run_game():
    pygame.init()

    ai_settings = Settings(pygame.image.load('Mushroom.png'))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    character = Character(ai_settings, screen)
    mushrooms = Group()
    gf.crete_new_mushroom(mushrooms, ai_settings, screen)

    stats = GameStats(ai_settings)

    while True:
        gf.check_events(ai_settings, screen, character)
        character.update()

        gf.update_screen(ai_settings, screen, character, mushrooms)
        gf.update_mushrooms(mushrooms)

        out_of_screen_deleted_count = gf.remove_out_of_screen_mushrooms(mushrooms)
        if out_of_screen_deleted_count != 0:
            gf.crete_new_mushroom(mushrooms, ai_settings, screen)
            stats.character_lives -= 1
            if stats.character_lives == 0:
                sys.exit()

        collisions_deleted_count = gf.remove_mushrooms_collided(character, mushrooms)
        if collisions_deleted_count != 0:
            gf.crete_new_mushroom(mushrooms, ai_settings, screen)


run_game()