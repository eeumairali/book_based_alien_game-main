class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        self.ship_speed_factor = 1

        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0,0,0)

        # Game settings
        self.ship_limit = 3

        # Alien settings
        self.alien_speed_factor = 0.5
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        self.fleet_drop_speed = 10

        # Game speedup (increase difficulty after each wave)
        self.speedup_scale = 1.1
