import sys
import os
import threading

import pygame

import obj.scene


class _MoveThread(threading.Thread):
    def __init__(self, sprite):
        super().__init__()
        # self.sprite 传入指针

        self.sprite: obj.Sprite.Sprite = sprite
        self.clock = pygame.time.Clock()

    def run(self):

        # 计算移动速度
        distance_x = abs(self.sprite.rect[0] - self.sprite._new_position[0])

        distance_y = abs(self.sprite.rect[1] - self.sprite._new_position[1])

        speed_y = distance_y / self.sprite._milliseconds / self.sprite.game.setting_dict["Run_clock"]
        speed_x = distance_x / self.sprite._milliseconds / self.sprite.game.setting_dict["Run_clock"]

        while self.sprite.rect:
            if self.sprite.rect[0] < self.sprite._new_position[0]:
                self.sprite.rect[0] += speed_x
            else:
                self.sprite.rect[0] -= speed_x

            if self.sprite.rect[1] < self.sprite._new_position[1]:
                self.sprite.rect[1] += speed_y
            else:
                self.sprite.rect[1] -= speed_y

            self.clock.tick(self.sprite.game.setting_dict["Run_clock"])


# 精灵类 Scene的派生类
class Sprite(obj.scene.Scene):
    def __init__(self, game, name, models, model):
        super().__init__(game, name, models, model)
        self._milliseconds = None
        self._new_position = None
        self.__move_thread_obj: threading.Thread = _MoveThread(self)

    def sprite_run(self):
        pass

    # 以下是触发器 等待被重写

    def script(self):
        pass

    def move_to(self, new_position: tuple or list, speed: float = None):
        if speed is None:
            self.rect.move_to(new_position)
        else:
            if self.rect[0] != new_position[0]:
                if self.rect[0] < new_position[0]:
                    self.rect[0] += speed
                else:
                    self.rect[0] -= speed

            if self.rect[1] != new_position[1]:
                if self.rect[1] < new_position[1]:
                    self.rect[1] += speed
                else:
                    self.rect[1] -= speed

    def move_in_milliseconds(self, new_position: list or tuple, milliseconds: int):
        """
        在毫秒内移动到某一个位置 （开启多线程）
        :param new_position: 目标坐标 float[]
        :param milliseconds: 毫秒
        :return: None
        """
        self._new_position = new_position
        self._milliseconds = milliseconds
        self.__move_thread_obj.start()
