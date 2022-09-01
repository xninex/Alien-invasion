import sys
import pygame as pg
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.aliens = pg.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Запуск основного цикла"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullet()
            self._update_aliens()
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
        """Создание нового снаряда и вложение его в группу bullets"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullet(self):
        self.bullets.update()
        # Удаление старых снарядов
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)


    def _update_screen(self):
        # При каждом проходе цикла перерисовывается экран
        self.screen.blit(self.settings.fon, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # Отображение последнего перерисованного экрана
        pg.display.flip()


    def _create_fleet(self):
        """Создает флот пришельцев"""
        alien = Alien(self)
        alien_width, alien_hight = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        """Определяет количество рядов, помещающихся н аэкране"""
        ship_heigt = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_hight) - ship_heigt)
        number_rows = available_space_y // (2* alien_hight)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        """Создание пришельца и размещение его в ряду"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()


    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление флота"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1




if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
