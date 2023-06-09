import pygame

class Bird:
    def __init__(self,game):
        super().__init__()
        self.settings = game.settings
        self.image = pygame.image.load("picture/bird.bmp").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.settings.bird_width, self.settings.bird_height))
        self.rect_image = self.image.get_rect()
        self.rect = pygame.Rect(0,0,self.settings.rect_bird_width,self.settings.rect_bird_height)
        self.rect.x = 500
        self.rect.y = 500
        self.y = self.rect.y
        self.screen = game.screen
        self.speed_fall = 0
        self.angle = 0
        #dźwiek
        self.sound = game.sound
        self.jump_sound = pygame.mixer.Sound("sound/flap_3.wav")


    def show_bird(self):
        self.rotated_image=pygame.transform.rotate(self.image,self.angle)
        new_rect = self.rotated_image.get_rect(center=self.image.get_rect(center=self.rect.center).center)

        self.screen.blit(self.rotated_image, new_rect)

    def update_bird(self):
        if self.speed_fall < self.settings.max_speed_fall:
            self.speed_fall += 0.01
        self.y += self.speed_fall
        self.rect.y = self.y
        if self.angle>-90:
            self.angle-=self.settings.rising_angle

    def set_bird(self):
        self.rect.y = 500
        self.rect_image.y = 500
        self.y = self.rect.y
        self.angle = 0

    def jump(self):
        self.speed_fall = self.settings.jump_speed
        self.angle = 90
        if self.sound:
            self.jump_sound.play()
