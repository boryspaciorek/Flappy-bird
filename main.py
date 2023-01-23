import pygame
import time
from sys import exit
from settings import Settings
from bird import Bird
class Game:
    """classa główna"""
    def __init__(self):
        pygame.init()
        self.settings=Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen_rect=self.screen.get_rect()
        self.settings.screen_height=self.screen_rect.height
        self.settings.screen_width = self.screen_rect.width
        self.bird=Bird(self)

    def start_game(self):
        """funkcja główna"""

        while True:
            #time.sleep(0.2)
            self.events()
            self.update_screen()
            self.bird.update_bird()



    def events(self):
        """sprawdza rodzaj sytuacji"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._event_down(event)
            elif event.type == pygame.KEYUP:
                self._event_up(event)
            elif event.type == pygame.QUIT:
                exit()


    def _event_down(self,event):
        """sprawdza wciśnietę klawisze"""
        if event.key == pygame.K_SPACE:
            self.bird.jump( )


    def _event_up(self,event):
        """sprawdza puszczone klawisze"""
        if event.key==pygame.K_ESCAPE:
            exit()

    def update_screen(self):
        self.bird.show_bird()
        pygame.display.flip()
        self.screen.fill((40,40,40))


if __name__=="__main__":
    ai = Game()
    ai.start_game()