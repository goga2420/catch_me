import pygame

class Character:
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('mario-bit-map.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.left = self.screen_rect.left

        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.character_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.character_speed_factor
        if self.moving_up and self.rect.up > 0:
            self.center -= self.ai_settings.character_speed_factor
        if self.moving_down and self.rect.down < self.screen_rect.down:
            self.center += self.ai_settings.character_speed_factor


    def blitme(self):
        self.screen.blit(self.image, self.rect)
