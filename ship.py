import pygame

class Ship():

    def __init__(self, screen):
        """ Initializes the ship with start coordinates."""
        self.screen = screen

        # Loading starship image
        self.image = pygame.image.load('images/ship-0.bmp')
        self.rect = self.image.get_rect()


