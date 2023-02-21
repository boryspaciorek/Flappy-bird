import pygame
from random import randint
from sys import exit
from settings import Settings
from bird import Bird
from background import Background
from background import Line_on_the_bottom
from tube import Tube_bottom,Tube_top
class Game:
    """classa główna"""
    def __init__(self):
        #ustawienia ogólne
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()
        self.settings.screen_height = self.screen_rect.height
        self.settings.screen_width = self.screen_rect.width
        #ptak
        self.bird = Bird(self)
        self.background = Background(self)
        #zielona linia tworząca iluzje poruszania się
        self.lines = [Line_on_the_bottom(self,0)]
        self.lines.append(Line_on_the_bottom(self,self.lines[0].image_rect.right-16))
        #rury
        self.tubes_bottom = pygame.sprite.Group()
        self.tubes_top = pygame.sprite.Group()


    def start_game(self):
        """funkcja główna"""

        while True:
            #time.sleep(0.2)
            self.events()
            self.update_screen()
            self.move_bird()
            self.move_lines()
            self.move_tubes()
            self.add_tubes()

    def events(self):
        """sprawdza rodzaj sytuacji"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._event_down(event)
            elif event.type == pygame.KEYUP:
                self._event_up(event)
            elif event.type == pygame.QUIT:
                exit()

    def move_bird(self):
        self.bird.update_bird()
        self._check_bird()

    def _check_bird(self):
        if self.bird.rect.y < 0:
            self.bird.speed_fall = 0
            self.bird.angle = -45

    def _event_down(self,event):
        """sprawdza wciśnietę klawisze"""
        if event.key == pygame.K_SPACE:
            self.bird.jump( )


    def _event_up(self,event):
        """sprawdza puszczone klawisze"""
        if event.key==pygame.K_ESCAPE:
            exit()

    def update_screen(self):
        #uaktualnia ekran
        self.background.show_background()
        self._show_all_lines()
        self.bird.show_bird()
        self._show_tubes()
        pygame.display.flip()

        self.screen.fill((40,40,40))


    def _show_tubes(self):
        """pokazuje tuby"""
        self.tubes_bottom.draw(self.screen)
        self.tubes_top.draw(self.screen)


    def move_lines(self):
        """porusza zieloną linią"""
        for i in self.lines:
            i.move_line()
            if i.image_rect.right < 0:
                i.change_place_line(self.i.rect.width)

    def _show_all_lines(self):
        for i in self.lines:
            i.show_line()

    def move_tubes(self):
        self.tubes_bottom.update()
        self.tubes_top.update()
        self._check_border()

    def _check_border(self):
        """sprawdza czy rura wyszła poza ekran"""
        for i in range(len(self.tubes_top)):
            if self.tubes_top.sprites()[i].rect.right<0:
                self.tubes_top.remove(self.tubes_top.sprites()[i])
                self.tubes_bottom.remove(self.tubes_bottom.sprites()[i])
                break

    def add_tubes(self):
        if not self.tubes_top or self.tubes_top.sprites()[-1].rect.right + self.settings.space_between_next_tube < self.screen_rect.width:
            random=randint(100,900)
            bottom_tube = Tube_bottom(self, random)
            top_tube=Tube_top(self, bottom_tube.rect.y - self.settings.space_between_tube)
            self.tubes_top.add(top_tube)
            self.tubes_bottom.add(bottom_tube)
            print(len(self.tubes_top))

if __name__=="__main__":
    ai = Game()
    ai.start_game()