class GameStats:
    """A class for tracking game statistic"""
    def __init__(self, game):
        self.high_score = 0
        self.settings = game.settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
