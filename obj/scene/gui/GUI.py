import pygame

from obj.scene.Sprite import Sprite


class GUI(Sprite):
    def __init__(self, game, name, models, model):
        super().__init__(game, name, models, model)
        self.location_offset = None
        self.GUI_location = None

    def when_window_resize_run(self):
        self.set_location()
        self.__is_changed = True

    def scale_run(self):
        if self.game.setting_dict["UI_scaling"] != False:
            scaling = int(self.game.setting_dict["UI_scaling"])
            self.set_width(self.get_width() + scaling)
            self.set_height(self.get_height() + scaling)
            self.set_location()

    def set_location(self, GUI_location=None, offset: tuple or list = None):
        if GUI_location is not None:
            self.GUI_location = GUI_location

        if offset is not None:
            self.location_offset = offset

        size = pygame.display.get_window_size()
        if self.GUI_location == CENTER:
            self.position[0] = size[0] / 2 - self.get_width() / 2
            self.position[1] = size[1] / 2 - self.get_height() / 2
        elif self.GUI_location == DIRECTLY_BELOW:
            self.position[0] = size[0] / 2 - self.get_width() / 2
            self.position[1] = size[1] - self.get_height()
        elif self.GUI_location == DIRECTLY_ABOVE:
            self.position[0] = size[0] / 2 - self.get_width() / 2
            self.position[1] = 0
        elif self.GUI_location == UPPER_RIGHT:
            self.position[0] = 0
            self.position[1] = 0
        elif self.GUI_location == LOWER_RIGHT:
            self.position[0] = 0
            self.position[1] = size[1] - self.get_height()
        elif self.GUI_location == UPPER_LEFT:
            self.position[0] = size[0] - self.get_width()
            self.position[1] = 0
        elif self.GUI_location == LOWER_LEFT:
            self.position[0] = size[0] - self.get_width()
            self.position[1] = size[1] - self.get_height()
        if offset is not None:
            self.position[0] += offset[0]
            self.position[1] += offset[1]


CENTER = "CENTER"
DIRECTLY_ABOVE = "DIRECTLY_ABOVE"
DIRECTLY_BELOW = "DIRECTLY_BELOW"
UPPER_LEFT = "UPPER_LEFT"
LOWER_LEFT = "LOWER_LEFT"
UPPER_RIGHT = "UPPER_RIGHT"
LOWER_RIGHT = "LOWER_RIGHT"
