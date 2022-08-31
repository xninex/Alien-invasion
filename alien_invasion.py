import sys
import pygame as pg
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion():

    def __init__(self):
        pg.init()
        self.settings = Settings()
        self.screen = pg.display.set_mode(
            (self.settings.screen_width,self.settings.screen_height))

        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pg.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pg.sprite.Group()

    def run_game(self):
        """Запуск основного цикла"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()


    def _check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            elif event.type == pg.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pg.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Нажатие клавиш"""
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pg.K_UP:
            self.ship.moving_up = True
        elif event.key == pg.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pg.K_q:
            sys.exit()
        elif event.key == pg.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        """Отпускание клавиш"""
        if event.key == pg.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pg.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pg.K_UP:
            self.ship.moving_up = False
        elif event.key == pg.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        # При каждом проходе цикла перерисовывается экран
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Отображение последнего перерисованного экрана
        pg.display.flip()



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
