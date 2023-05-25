from time import sleep
import pygame
from random import randint
from sys import exit
from settings import Settings
from bird import Bird
from background import Background
from background import Line_on_the_bottom
from tube import Tube_bottom, Tube_top, End_tube, Line_between_tube
from points import Points
from button import Button



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
        # dźwiek
        self.sound = True
        #ptak
        self.bird = Bird(self)
        self.bird.set_bird()
        #tło
        self.background = Background(self)
        #zielona linia tworząca iluzje poruszania się
        self.lines = [Line_on_the_bottom(self,0)]
        self.lines.append(Line_on_the_bottom(self,self.lines[0].image_rect.right-16))
        #rury
        self.tubes_bottom = pygame.sprite.Group()
        self.tubes_top = pygame.sprite.Group()
        self.end_tubes = pygame.sprite.Group()
        self.tubes_points = pygame.sprite.Group()
        #pkt
        self.points = Points(self)
        #włączenie gry
        self.death = False
        self.run_game = False
        self.moving_bird = False
        self.falling_bird = False
        self.play_button = Button(self)
        #dźwiek
        self.death_sound = pygame.mixer.Sound("sound/die.wav")
        self.hit_sound = pygame.mixer.Sound("sound/hit.wav")
        self.hit_count = 0 #służy do tego żeby dźwiek włączył się tylko raz




    def start_game(self):
        """funkcja główna"""
        while True:
            #time.sleep(0.2)
            self.events()
            self.update_screen()
            if self.run_game:
                self.move_bird()
                if self.moving_bird:
                    self.move_tubes()
                    self.add_tubes()
                    self.move_lines()


    def events(self):
        """sprawdza rodzaj sytuacji"""
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self._event_down(event)
            elif event.type == pygame.KEYUP:
                self._event_up(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.check_buttons_hold()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.check_buttons_release()
            elif event.type == pygame.QUIT:
                exit()

    def move_bird(self):
        """zarządza ptakiem"""
        if self.falling_bird:
            self.bird.update_bird()
            self._check_bird()

    def _check_bird(self):
        """sprawdza czy ptak nie wychodzi poza mapę"""
        if self.bird.rect.y + self.bird.speed_fall < 0:
            self.bird.speed_fall = 0
            self.bird.angle = -45
        self._check_colision_tube_bird()

    def _event_down(self,event):
        """sprawdza wciśnietę klawisze"""
        if event.key == pygame.K_SPACE:
            self.falling_bird = True
            if not self.death:
                self.moving_bird = True
                self.bird.jump( )


    def _event_up(self,event):
        """sprawdza puszczone klawisze"""
        if event.key==pygame.K_ESCAPE:
            exit()

    def update_screen(self):
        """uaktualnia ekran"""
        pygame.display.flip()
        self.background.show_background()
        self._show_all_lines()

        if self.run_game:
            self._show_tubes()
            self.points.show_points()
            self.bird.show_bird()
        else:
            self.play_button.show_button()


    def _show_tubes(self):
        """pokazuje tuby"""
        self.tubes_bottom.draw(self.screen)
        self.tubes_top.draw(self.screen)
        self.end_tubes.draw(self.screen)


    def move_lines(self):
        """porusza zieloną linią"""
        for i in self.lines:
            i.move_line()
            if i.image_rect.right < 0:
                i.change_place_line(i.image_rect.width)

    def _show_all_lines(self):
        """pokazuje dolne linie"""
        for i in self.lines:
            i.show_line()

    def move_tubes(self):
        """porusza tubami"""
        self.tubes_bottom.update()
        self.tubes_top.update()
        self.end_tubes.update()
        self.tubes_points.update()
        self._check_border()

    def _check_border(self):
        """sprawdza czy rura wyszła poza ekran"""
        for i in range(len(self.tubes_top)):
            if self.tubes_top.sprites()[i].rect.right<0:
                self.tubes_top.remove(self.tubes_top.sprites()[i])
                self.tubes_bottom.remove(self.tubes_bottom.sprites()[i])
                self.end_tubes.remove(self.tubes_bottom.sprites()[i])
                self.end_tubes.remove(self.tubes_bottom.sprites()[i])
                break
        collision = pygame.sprite.spritecollideany(self.bird, self.tubes_points,)
        if collision:
            self.tubes_points.remove(collision)
            self.points.update()

    def add_tubes(self):
        """dodaje tube"""
        if not self.tubes_top or \
                self.tubes_top.sprites()[-1].rect.right + self.settings.space_between_next_tube < self.screen_rect.width:
            random=randint(350,800)
            bottom_tube = Tube_bottom(self, random)
            top_tube=Tube_top(self, bottom_tube.rect.y - self.settings.space_between_tube)
            end_tube_bottom = End_tube(self, bottom_tube.rect.y)
            end_tube_top = End_tube(self, top_tube.rect.bottom,False)
            tube_point=Line_between_tube(self, random - self.settings.space_between_tube)
            self.tubes_top.add(top_tube)
            self.tubes_bottom.add(bottom_tube)
            self.end_tubes.add(end_tube_bottom)
            self.end_tubes.add(end_tube_top)
            self.tubes_points.add(tube_point)

    def _check_colision_tube_bird(self):
        """sprawdza możliwości śmierci"""
        collision_top = pygame.sprite.spritecollideany(self.bird, self.tubes_top)
        collision_bottom = pygame.sprite.spritecollideany(self.bird, self.tubes_bottom)
        if collision_bottom or collision_top:
            self.hit_tube()
            if self.sound and self.hit_count == 0:
                self.hit_sound.play()
                self.hit_count += 1
        if self.bird.rect.bottom > self.lines[0].image_rect.y:
            self.hit_count = 0
            self.die()

    def hit_tube(self):
        self.settings.clear_setings()
        self.moving_bird = False
        self.death = True

    def check_buttons_hold(self):
        """sprawdza czy guziki są wciśniete"""
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.rect.collidepoint(mouse_pos):
            self.play_button.hold_button()

    def check_buttons_release(self):
        """sprawdza czy guzik został puszczony"""
        if self.play_button.button_click:
            self.play_button.release_button()
            mouse_pos = pygame.mouse.get_pos()
            #jeśli został wciśniety to sprawdza czy jest puszczany na obszarze przycisku
            if self.play_button.rect.collidepoint(mouse_pos):
                self.death = False
                self.run_game = True
                self.settings.reset_settings()

    def _clear_tube(self):
        self.tubes_top.empty()
        self.tubes_bottom.empty()
        self.tubes_points.empty()
        self.end_tubes.empty()

    def die(self):
        """odpowiada za to co się dzieje po śmierci gracza"""
        self.death_sound.play()
        sleep(0.5)
        self._clear_tube()
        self.bird.set_bird()
        self.points.reset_points()
        self.run_game = False
        self.falling_bird = False




if __name__=="__main__":
    ai = Game()
    ai.start_game()