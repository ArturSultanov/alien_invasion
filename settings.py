class Settings():
    """Class for saving settings of the game."""

    def __init__(self):
        """Initializes game settings. """
        # Screen parameters
        self.screen_width = 1024
        self.screen_height = 640
        self.bg_color = (40, 10, 50)

        # Ship speed
        self.ship_speed_factor = 1

        # Bullets param
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 200, 200, 200

