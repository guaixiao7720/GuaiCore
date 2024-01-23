import pygame

cdef class Surface:
    def set_alpha(self, int num):
        self.__alpha = num
        self.__is_changed = True