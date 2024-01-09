import copy

import pygame.font

import obj.GUI


class Text(obj.GUI.GUI):
    def __init__(self, game, name, text: str, size: int):
        super().__init__(game, name, None, None)
        self.__text = text
        self.__size = size
        self.__font: pygame.font.Font = copy.deepcopy(self.game.FONT)
        self.__font.set_point_size(self.__size)
        self.image = self.__font.render(self.__text, False, (0, 0, 0))

    def draw(self):
        self.game.screen.blit(self.image, self.rect)

    def set_text(self, text: str, antialias: bool, color: tuple or list, position, bg_color=None):
        self.__text = text
        self.__font: pygame.font.Font = copy.deepcopy(self.game.FONT)
        self.__font.set_point_size(self.__size)
        self.image = self.__font.render(self.__text, antialias, color, bg_color)
        self.rect = self.image.get_rect()
