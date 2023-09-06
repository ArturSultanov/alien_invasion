import pygame
# from pygame.sprite import Sprite


class Alien():
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading alien image
        self.image = pygame.transform.scale(
            pygame.image.load('images/ship-1.bmp'),
            (80, 76))
        self.rect = self.image.get_rect()
        # Every alien appears at the left top corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # self.x = float(self.rect.x)

    def blitme(self):
        """Draw alien at the screen"""
        self.screen.blit(self.image, self.rect)
