class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        self.ship_lives_left = self.ai_settings.ship_limit

