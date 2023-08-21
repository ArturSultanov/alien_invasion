import pygame


class Ship():

    def __init__(self, screen):
        """ Initializes the ship with start coordinates."""
        self.screen = screen

        # Loading starship image
        self.image = pygame.transform.scale(
                     pygame.image.load('images/ship-0.bmp'),
                     (80, 61))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Each new ship appears at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draws the ship at the current position."""
        self.screen.blit(self.image, self.rect)
