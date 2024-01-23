import json
import os
from typing import TextIO
from .. cimport Game

import pygame

cdef PATH = os.path.abspath("") + "/"


cdef public str load(Game.Game game):
    """读取GuaiCore设置文件"""

    # 后面需要修改 当前仅测试用
    cdef TextIO setting = open(f"{PATH}setting/{game}.json", "r")

    cdef str str1 = setting.readlines()[0]
    setting.close()

    return json.loads(str1)

def load_fonts():
    fonts_setting = open(f"{PATH}setting/fonts.json", "r")

    str1 = fonts_setting.readlines()[0]
    fonts_setting.close()
    fonts_setting_dict = json.loads(str1)
    fonts_setting = pygame.font.Font(f"{PATH}fonts/{fonts_setting_dict['1']}")

    return fonts_setting

def is_first_run():
    """检查引擎是否是第一次运行"""
    # 通过查看setting\hello.txt 的内容判断 请勿随便修改
    setting = open(f"../../setting/hello.txt", "r+")
    if setting.readlines()[0] == "True":
        setting.writelines(["False"])
        setting.close()
        return True
    elif setting.readlines()[0] == "False":
        setting.close()
        return False
