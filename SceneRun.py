import threading

import pygame


class SceneRun(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, game):

        threading.Thread.__init__(self)
        self.game = game
        self.is_stop = False
        self.clock = pygame.time.Clock()
        self.run_speed = 60
        self.game.running = True

    def run(self):
        while self.game.running:
            self.game.screen.fill(self.game.bg_color)
            self.game.main_scene.draw()
            pygame.display.flip()
            self.clock.tick(self.game.setting_dict["FPS_clock"])

