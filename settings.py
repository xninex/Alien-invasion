import pygame.image

class Settings():
    def __init__(self):
        #Разрешение окна
        self.screen_width = 1800
        self.screen_height = 1000

        #Цвет фона
        # self.bg_color = (48, 48, 48)

        self.fon = pygame.image.load('images/fon.bmp')

        #Скорость движения корабля
        self.ship_speed = 1.5

        #Параметры снаряда
        self.bullet_speed = 3
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_color = (255, 48, 48)
        self.bullet_allowed = 3

        # Настройка пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1




