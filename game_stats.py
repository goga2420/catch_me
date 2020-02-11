class GameStats:
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.character_lives = self.ai_settings.character_lives

    def reset_stats(self):
        self.character_lives = self.ai_settings.character_lives
