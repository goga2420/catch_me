class Settings:
    def __init__(self, objekt_image):
        self.title = "Alien Invasion"
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        self.character_speed_factor = 5
        self.character_limit = 3
        self.objekt_speed_factor = 1
        self.fleet_direction = 1
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.objekt_image = objekt_image
        self.objekt_rect = self.objekt_image.get_rect