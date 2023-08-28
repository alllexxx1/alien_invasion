class Settings:
    """A class for storing game settings"""
    def __init__(self):
        # Screen settings
        self.screen_width = 1700
        self.screen_height = 950
        self.bg_color = (85, 206, 250)

        # Ship settings
        self.ship_limit = 3

        # Bullets settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (216, 31, 42)
        self.bullets_allowed = 3

        # Aliens settings
        self.fleet_drop_speed = 10

        # Game acceleration pace
        self.speedup_scale = 1.3
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 4.7
        self.bullet_speed_factor = 7.0
        self.alien_speed_factor = 3.4
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
