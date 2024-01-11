import pygame


class Obj(pygame.sprite.Sprite):
    def __init__(self, game, name):
        super().__init__()
        self.__is_running = True
        self.game = game
        self.name = name

    def start(self):
        self.__is_running = True

    def stop(self):
        self.__is_running = False

    def get_running(self):
        return self.__is_running
