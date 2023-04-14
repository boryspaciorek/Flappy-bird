import pygame.font

class Points():
    def __init__(self,game):
        self.screen = game.screen
        self.screen_rect = game.screen_rect
        self.font = pygame.font.SysFont(None,48)
        self.points = 0
        self._prep_points()

    def reset_points(self):
        self.points = 0
        self._prep_points()

    def _prep_points(self):
        self.text = self.font.render(str(self.points),True,(0,0,0),None)
        self.rect = self.text.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.y = 10

    def update(self):
        self.points += 1
        self._prep_points()

    def show_points(self):
        self.screen.blit(self.text,self.rect)