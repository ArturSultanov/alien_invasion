import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading alien image
        self.image = pygame.transform.scale(
            pygame.image.load('images/ship-1.bmp'),
            (90, 75))
        # self.image = pygame.image.load('images/ship-1.bmp')
        self.rect = self.image.get_rect()
        # Every alien appears at the left top corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """Draw alien at the screen"""
        self.screen.blit(self.image, self.rect)
