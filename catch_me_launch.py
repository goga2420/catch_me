import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from objekt import Objekt
from character import Character
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings(pygame.image.load('Mushroom.png'))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    character = Character(ai_settings, screen)
    objekts = Group(Objekt(ai_settings, screen))

    while True:
        gf.check_events(ai_settings, screen, character)
        character.update()
        gf.update_screen(ai_settings, screen, character, objekts)
        gf.update_objekts(objekts, character)

run_game()