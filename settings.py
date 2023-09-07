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
        # Alien movement behaviour
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1


        # Bullets param
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 200, 250, 200

