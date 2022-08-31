import pygame.image

class Settings():
    def __init__(self):
        #Разрешение окна
        self.screen_width = 1800
        self.screen_height = 1000

        #Цвет фона
        self.bg_color = (48, 48, 48)

        # self.bg = pygame.image.load('images/fon.bmp')

        #Скорость движения корабля
        self.ship_speed = 1.5

        #Параметры снаряда

        self.bullet_speed = 3
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (255, 48, 48)
        self.bullet_allowed = 3


