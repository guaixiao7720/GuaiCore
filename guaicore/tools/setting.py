import json
import os

import pygame

PATH = os.path.abspath("") + "/"


def load(game: str):
    """读取GuaiCore设置文件"""

    # 后面需要修改 当前仅测试用
    setting = open(f"{PATH}setting/{game}.json", "r")

    str1 = setting.readlines()[0]
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
