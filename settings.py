class Settings():
    """ A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""

        # Screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (20,20,230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width =3
        self.bullet_height = 150
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 1 

        # Alien settings
        self.fleet_drop_speed = 1

        # How quickly the alien point values increase
        self.score_scale = 1.5
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialze settings that change through out the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor =1

        # Scoring
        self.alien_points = 50
        
        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction =1

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int (self.alien_points * self.score_scale)
        print(self.alien_points)
