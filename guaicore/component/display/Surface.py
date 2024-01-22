import pygame

class Surface:
    def set_alpha(self, num: int or None):
        self.__alpha = num
        self.__is_changed = True