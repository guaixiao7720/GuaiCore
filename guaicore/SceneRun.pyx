import platform
import threading

import pygame


cdef class SceneRun(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, game):

        threading.Thread.__init__(self)
        self.game = game
        self.is_stop = False
        self.clock = pygame.time.Clock()
        self.run_speed = 60
        self.game.running = True
        self.system_name = platform.system()
        print(f"当前系统：{self.system_name}")

    def run(self):
        while self.game.running:
            self.game.main_scene.run()
            self.clock.tick(self.game.setting_dict["Run_clock"])

    cdef public void test_run(self):
        self.game.main_scene.run()
        # self.clock.tick(self.game.setting_dict["Run_clock"])