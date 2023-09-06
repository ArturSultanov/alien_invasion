import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """ Initializes the ship with start coordinates."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading starship image
        self.image = pygame.transform.scale(
                     pygame.image.load('images/ship-0.bmp'),
                     (95, 72))
        # self.image = pygame.image.load('images/ship-0.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Each new ship appears at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Saving the float coordinates of the center of the ship.

        # Moving flag
        self.moving_right = False
        self.moving_left = False

    def update_moving(self):
        """Update ship position due to the 'Moving flag'."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
        # Updating self.rect.centerx attribute based on self.center.

    def blitme(self):
        """Draws the ship at the current position."""
        self.screen.blit(self.image, self.rect)
