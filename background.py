import pygame

class Background:
    def __init__(self, game):
        super().__init__()
        self.screen=game.screen
        self.image=pygame.image.load("picture/background.png")#
        self.image=pygame.transform.scale(self.image,(1536,864 ))#
        self.image_rect=self.image.get_rect()
        self.image_rect.topleft=(0,0)

    def show_background(self):
        self.screen.blit(self.image,self.image_rect)

class Line_on_the_bottom:
    def __init__(self, game,x):
        super().__init__()
        self.screen=game.screen
        self.image=pygame.image.load("picture/line_on_the_bottom.bmp").convert()
        self.image=pygame.transform.scale(self.image,(1536,16 ))
        self.image_rect=self.image.get_rect()
        self.image_rect.x = x
        self.x = x
        self.image_rect.y = 795
        self.speed = game.settings.speed


    def show_line(self):
        """pokazanie obrazu"""
        self.screen.blit(self.image,self.image_rect)

    def move_line(self):
        """poruszanie się obrazu"""
        self.x -= self.speed
        self.image_rect.x=self.x

    def change_place_line(self,x):
        self.x = x
        self.image_rect.x = x
