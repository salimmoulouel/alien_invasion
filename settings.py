class Settings:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        
        # ship settings
        self.ship_speed=4
        self.ship_limit=3# 

        # Bullet settings
        
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        

        # fleet settings
        self.fleet_drop_speed = 60
        

        # control game speed up
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ initialise the settings which will pross through the game"""
        # Alien settings 
        self.alien_speed = 1.0

        self.bullet_speed = 1.0

        self.ship_speed=4

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        self.alien_point = 50


    def increase_speed(self):
        """ increase dynamique settings through the game """
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.alien_point *= self.score_scale 

