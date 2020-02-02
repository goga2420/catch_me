import pygame
from pygame.sprite import Sprite


class Objekt(Sprite):
    def __init__(self, ai_settings, screen):
        super(Objekt, self).__init__()

        self.ai_settings = ai_settings
        self.screen = screen
        self.image = ai_settings.objekt_image

        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.center = float(self.rect.centerx)


    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def update(self):
        self.rect.y += self.ai_settings.objekt_speed_factor * self.ai_settings.objekt_speed_factor


    def check_bottom(self):
        if self.rect.bottom >= self.screen.get_rect().bottom:
            return True
