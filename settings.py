class Settings:
    def __init__(self, mushroom_image):
        self.title = "Mario"
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        self.character_speed_factor = 5
        self.character_lives = 3

        self.mushroom_speed_factor = 1
        self.mushroom_image = mushroom_image
        self.mushroom_rect = self.mushroom_image.get_rect
