import sys
import os

import pygame

import Obj.Scene


# 精灵类 Scene的派生类
class Sprite(Obj.Scene.Scene):
    def __init__(self, game, name, models, model):
        super().__init__(game, name, models, model)

    def sprite_run(self):
        pass

    # 以下是触发器 等待被重写

    def script(self):
        pass
