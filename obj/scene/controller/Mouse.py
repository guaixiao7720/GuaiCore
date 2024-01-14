import pygame

from obj.scene.Sprite import Sprite


class Mouse(Sprite):
    def __init__(self, game, name, width, height):
        super().__init__(game, name, {1: pygame.Surface((width, height))}, 1)
        self.rect = pygame.rect.Rect(0, 0, width, height)

    def run(self):
        mos = pygame.mouse.get_pos()
        self.rect[0] = mos[0]
        self.rect[1] = mos[1]

