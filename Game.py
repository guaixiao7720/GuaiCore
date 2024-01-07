import copy

import pygame
import threading

import Obj.Scene
import Tools.Setting
from SceneRun import SceneRun


def new_game(name: str, screen: pygame.Surface):
    return Game(name, screen=screen)


class Game:

    def __init__(self, name: str, screen: pygame.Surface):
        self.PATH = None
        self.running = None
        self.screen = screen
        self.name = name
        self.FPS_clock = pygame.time.Clock()
        self.setting_dict = Tools.Setting.load(self.name)
        self.bg_color = [255, 255, 255]
        self.event = {
            "MOUSEBUTTONDOWN": False,
            "MOUSEBUTTONUP": False,

            }


        self.main_scene = Obj.Scene.Scene(self, "main")
        self.main_scene.is_running = True
        self.main_scene.view = True

        # 主run线程
        self.main_running = SceneRun(self)
        self.main_running.start()

    def scene_append(self, sprite):
        self.main_scene.tree.append(copy.copy(sprite))

    def start(self):
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    self.running = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.event["MOUSEBUTTONDOWN"] = True
                else:
                    self.event["MOUSEBUTTONDOWN"] = False

                if event.type == pygame.MOUSEBUTTONUP:
                    self.event["MOUSEBUTTONUP"] = True
                else:
                    self.event["MOUSEBUTTONUP"] = False

            self.main_scene.run()

            self.FPS_clock.tick(512)  # limits FPS to 60

        del self.main_running
        pygame.quit()
