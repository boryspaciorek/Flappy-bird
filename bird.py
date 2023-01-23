import pygame

class Bird:
    def __init__(self,game):
        super().__init__()
        self.settings = game.settings
        self.image = pygame.image.load("picture/bird.bmp")
        self.image = pygame.transform.scale(self.image, (self.settings.bird_width, self.settings.bird_height))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500
        self.y = self.rect.y
        self.screen = game.screen
        self.speed_fall = 0
        self.angle = -45


    def show_bird(self):
        self.rotated_image=pygame.transform.rotate(self.image,self.angle)
        new_rect = self.rotated_image.get_rect(center=self.image.get_rect(topleft=self.rect.topleft).center)

        self.screen.blit(self.rotated_image, new_rect)

    def update_bird(self):
        if self.speed_fall < self.settings.max_speed_fall:
            self.speed_fall += 0.01
        self.y += self.speed_fall
        self.rect.y = self.y
        if self.angle>-90:
            self.angle-=self.settings.rising_angle


    def jump(self):
        self.speed_fall = self.settings.jump_speed
        self.angle = 90
