import copy

import pygame.font

import obj.GUI


class Text(obj.GUI.GUI):
    def __init__(self, game, name, text: str, size: int):
        super().__init__(game, name, None, None)
        self.__text = text
        self.__size = size
        self.__font: pygame.font.Font = self.game.FONT
        self.__font.set_point_size(self.__size)
        self.image = self.__font.render(self.__text, False, (0, 0, 0))

    def draw(self):
        self.game.screen.blit(self.image, self.rect)

    def set_text(self, text: str, size: int, antialias: bool, color: tuple or list, position, bg_color=None):
        """
        设置该Text对象相关 建议实例化后都执行一次
        :param text: 文字字符串
        :param size: 大小
        :param antialias:
        :param color: 颜色
        :param position: 位置 仅支持 pygame.rect.Rect
        :param bg_color: 背景色 默认 NONE
        :return:
        """
        self.__text = text
        self.__size = size
        self.__font: pygame.font.Font = self.game.FONT
        self.__font.set_point_size(self.__size)
        self.image = self.__font.render(self.__text, antialias, color, bg_color)
        self.rect = self.image.get_rect()
