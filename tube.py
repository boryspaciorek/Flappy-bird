import pygame
from pygame.sprite import Sprite

class Tube_bottom(Sprite):
    def __init__(self, game,y):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.speed = game.settings.tube_speed
        self.image = pygame.image.load("picture/main_part_tube.bmp").convert()
        self.image = pygame.transform.scale(self.image,(game.settings.tube_width,game.settings.screen_height-y))
        self.rect = self.image.get_rect()
        self.rect.left = self.screen_rect.right
        self.rect.y = y
        self.x = self.rect.x

    def update(self):
        """poruszanie rur"""

        self.x -= self.speed
        self.rect.x = self.x


class Tube_top(Tube_bottom):
    """górna tuba"""
    def __init__(self,game,y):
        super().__init__(game,y)
        #self.image = pygame.transform.rotate(self.image,180)
        self.image = pygame.transform.scale(self.image, (game.settings.tube_width,y))
        self.rect = self.image.get_rect()
        self.rect.bottom = y


class End_tube(Sprite):
    """końcówka rury"""
    def __init__(self, game, y,bottom=True):
        super().__init__()
        self.image = pygame.image.load("picture/tube_end.bmp").convert()
        self.image = pygame.transform.scale(self.image, (game.settings.tube_width, 30))
        self.speed = game.settings.tube_speed
        self.rect = self.image.get_rect()
        self.rect.left = game.settings.screen_width
        self.x = game.settings.screen_width
        if bottom:
            self.rect.y = y
        else:
            self.rect.bottom=y

    def update(self):
        """poruszanie końcówki rur"""

        self.x -= self.speed
        self.rect.x = self.x


class Line_between_tube(Sprite):
    """służy do liczenia sprawdzenia czy ptak znajduje się miedzy rurami żeby można było zliczyć punkty"""
    def __init__(self,game,y1):
        super().__init__()
        #stworzenie prostokątu do zliczania pkt
        self.rect = pygame.Rect(game.settings.tube_width+game.settings.screen_width,
                                            y1, 1, game.settings.space_between_tube)
        self.x = game.settings.tube_width+game.settings.screen_width
        self.speed = game.settings.tube_speed

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    