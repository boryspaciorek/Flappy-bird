import pygame


class Button:

    def __init__(self, game):
        self.screen = game.screen
        self.button_width = game.settings.play_button_width
        self.button_height = game.settings.play_button_height
        self.image = pygame.image.load("picture/play_button.bmp").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.button_width, self.button_height))
        self.rect = self.image.get_rect()
        self.rect.height -= 3
        self.rect.width -= 12
        self.rect.centerx = game.settings.screen_width / 2 - 150
        self.rect.centery = game.settings.screen_height / 2 + 50
        self.button_click = False

    def show_button(self):
        """pokazanie guzika"""
        self.screen.blit(self.image, self.rect)

    def hold_button(self):
        self.rect.y += 10
        self.button_click = True

    def release_button(self):
        self.rect.y -= 10
        self.button_click = False
"""zrobić osobno rect i rect image żeby można było lepiej skalibrować klikniecia"""