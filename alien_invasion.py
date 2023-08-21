import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    # Initializes  pygame, settings and creates a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Ship creation
    ship = Ship(screen)

    # Starting the main game cycle.
    while True:
        # Tracking keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()


run_game()
