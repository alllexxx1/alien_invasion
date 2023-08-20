class GameStats:
    """Tracking stats for the game"""
    def __init__(self, game):
        self.settings = game.settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit