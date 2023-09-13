import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_functions import *
from game_stats import GameStats
from button import Button


def run_game():
    # Initializes  pygame, settings and creates a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)
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
        if stats.game_active:
            ship.update_moving()
            update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
            update_bullets(ai_settings, screen, ship, bullets, aliens)

        update_screen(ai_settings, screen, stats, ship, aliens, bullets,
                      play_button)


run_game()
