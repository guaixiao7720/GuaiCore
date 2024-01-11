import copy
import os
import platform
import sys

import pygame
import threading

import obj
import tools
from SceneRun import SceneRun


def new_game(name: str, screen: pygame.Surface):
    return Game(name, screen=screen)


class Game:

    def __init__(self, name: str, screen: pygame.Surface):
        self.PATH = None
        self.running = None
        self.screen = screen
        self.name = name
        self.RUN_clock = pygame.time.Clock()
        self.setting_dict = tools.setting.load(self.name)
        self.bg_color = [0, 0, 0]
        self.event = {
            "MOUSEBUTTONDOWN": False,
            "MOUSEBUTTONUP": False,
            "WINDOWRESIZED": False,
            "TEXTINPUT": False,

        }
        self.PATH = os.path.abspath(".") + "/"

        # 字体字典
        self.FONT = tools.setting.load_fonts()

        self.main_scene = obj.scene.Scene(self, "main")
        self.main_scene.is_running = True
        self.main_scene.view = True

        # 临时
        self.setting_dict["Run_clock"] = 512

        # 主run线程
        self.main_running = SceneRun(self)
        self.main_running.start()

    def scene_append(self, sprite):
        self.main_scene.tree.append(copy.copy(sprite))

    def start(self):
        self.running = True

        while self.running:
            self.__event_manager()

            self.screen.fill(self.bg_color)

            if not self.event["WINDOWRESIZED"]:
                # 运行主场景
                self.main_scene.draw()

            if platform.system() == "Windows":
                pygame.display.flip()
            elif platform.system() == "Linux":
                pygame.display.update()

            self.RUN_clock.tick(self.setting_dict["FPS_clock"])  # limits FPS to 60

        del self.main_running
        pygame.quit()
        sys.exit()

    def __event_manager(self):
        for event in pygame.event.get():
            self.event_obj = event
            if event.type == pygame.QUIT:
                self.running = False
            else:
                self.running = True

            if event.type == pygame.WINDOWRESIZED:
                self.event["WINDOWRESIZED"] = True
                self.main_scene.when_window_resize_run()
            else:
                self.event["WINDOWRESIZED"] = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.event["MOUSEBUTTONDOWN"] = True
            else:
                self.event["MOUSEBUTTONDOWN"] = False

            if event.type == pygame.MOUSEBUTTONUP:
                self.event["MOUSEBUTTONUP"] = True
            else:
                self.event["MOUSEBUTTONUP"] = False

            self.main_scene.event_run()
