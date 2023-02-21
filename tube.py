import pygame
from pygame.sprite import Sprite

class Tube_bottom(Sprite):
    def __init__(self, game,y):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.speed = game.settings.tube_speed
        self.image = pygame.image.load("picture/tube.png")
        self.image = pygame.transform.scale(self.image,(game.settings.tube_width,game.settings.tube_height))
        self.rect = self.image.get_rect()
        self.rect.right = self.screen_rect.right
        self.rect.y=y
        self.x = self.rect.x

    def update(self):
        """poruszanie rur"""
        self.x -= self.speed
        self.rect.x = self.x


class Tube_top(Tube_bottom):
    def __init__(self,game,y):
        super().__init__(game,y)
        self.image=pygame.transform.rotate(self.image,180)
        self.rect.bottom=y