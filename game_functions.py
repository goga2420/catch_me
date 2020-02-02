from random import randint
import sys
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



def prepare_objekt(objekt, objekt_number, row_number):
    object_width = objekt.rect.width
    objekt.rect.x = object_width + 2 * object_width * objekt_number
    objekt.rect.y = objekt.rect.height + 2 * objekt.rect.height * row_number

    random_factor = 40
    objekt.rect.x += randint(-random_factor, random_factor)
    objekt.rect.y += randint(-random_factor, random_factor)



def get_number_objekt_x(screen_width, objekt_width):
    available_space_x = screen_width - 2 * objekt_width
    number_object_x = int(available_space_x / (2 * objekt_width))
    return number_object_x


def update_objekts(objekts, character):
    objekts.update()
    remove_out_of_screen_objekts(objekts)
    collisions = pygame.sprite.groupcollide(character, objekts, True, True)
    if len(objekts) == 0:




def remove_out_of_screen_objekts(objekts):
    for a in objekts:
        if a.check_bottom():
            objekts.remove(a)

def update_screen(ai_settings, screen, charater, objekt):
    screen.fill(ai_settings.bg_color)
    charater.blitme()
    objekt.blitme()
    pygame.display.flip()