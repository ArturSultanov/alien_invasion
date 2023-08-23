import sys
import pygame


def check_events(ship):
    """Handles keystrokes and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right.
                ship.rect.centerx += 1


def update_screen(ai_settings, screen, ship):
    """Updates the images on the screen and displays a new screen."""
    # The screen is redrawn every time the loop passes.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()

