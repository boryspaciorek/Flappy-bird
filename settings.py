class Settings:
    def __init__(self):
        #ustawienia ekranu
        self.screen_width = 600
        self.screen_height = 1000
        #ustawienia ptaka
        self.bird_height = 120
        self.bird_width = 120
        self.rect_bird_height = 60
        self.rect_bird_width = 60
        self.max_speed_fall = 2
        self.jump_speed  = -2
        self.rising_angle = 0.3
        #ustawienia tła
        self.speed=0.2
        #ustawienia rur
        self.tube_width=100
        self.tube_height=200
        self.tube_speed = 0.8
        self.space_between_tube = 300 #miejsce miedzy rurą górną i dolną
        self.space_between_next_tube = 400#miejsce mierdzy każdą kolejną rurą
        #przyciski
        self.play_button_width = 175
        self.play_button_height = 100

    def reset_settings(self):
        self.tube_speed = 0.8
        self.speed = 0.2
        self.rising_angle = 0.3

    def clear_setings(self):
        self.tube_speed = 0
        self.speed = 0
        self.rising_angle = 0.6