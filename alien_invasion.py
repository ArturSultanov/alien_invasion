import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_functions import *


def run_game():
    # Initializes  pygame, settings and creates a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Ship creation
    ship = Ship(ai_settings, screen)

    # Alien creation
    # alien = Alien(ai_settings, screen)
    aliens = Group()
    # Alien fleet creation
    create_fleet(ai_settings, screen, ship, aliens)

    # Bullets group
    bullets = Group()

    # Starting the main game cycle.
    while True:
        # Tracking keyboard and mouse events.
        check_events(ai_settings, screen, ship, bullets)
        ship.update_moving()

        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        # print(len(bullets))

        update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
