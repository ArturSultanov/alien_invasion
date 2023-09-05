import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class representing a alien."""
    def __int__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading alien image
        self.image = pygame.transform.scale(
            pygame.image.load('images/ship-2.bmp'),
            (80, 61))
        self.rect = self.image.get_rect()
        # Every alien appears at the left top corner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw alien at the screen"""
        self.screen.blit(self.image, self.rect)
