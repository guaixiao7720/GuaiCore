import pygame

import obj.Sprite


class GUI(obj.Sprite):
    def __init__(self, game, name, models, model):
        super().__init__(game, name, models, model)
        self.location_offset = None
        self.GUI_location = None

    def when_window_resize_run(self):
        self.set_location()

    def scale_run(self):
        if self.game.setting_dict["UI_scaling"] != False:
            scaling = int(self.game.setting_dict["UI_scaling"])
            self.image = pygame.transform.scale(self.models_bac[self.image_name], (self.models_bac[self.image_name].get_size()[0] + scaling, self.models_bac[self.image_name].get_size()[1] + scaling))
            for key in self.models.keys():
                self.models[key] = pygame.transform.scale(self.models_bac[key], (self.models_bac[key].get_size()[0] + scaling, self.models_bac[key].get_size()[1] + scaling))
            self.set_location()

    def set_location(self, GUI_location=None, offset: tuple or list = None):
        if GUI_location is not None:
            self.GUI_location = GUI_location

        if offset is not None:
            self.location_offset = offset

        size = pygame.display.get_window_size()
        if self.GUI_location == CENTER:
            self.rect[0] = size[0] / 2 - self.image.get_size()[0] / 2
            self.rect[1] = size[1] / 2 - self.image.get_size()[1] / 2
        elif self.GUI_location == DIRECTLY_BELOW:
            self.rect[0] = size[0] / 2 - self.image.get_size()[0] / 2
            self.rect[1] = size[1] - self.image.get_size()[1]
        elif self.GUI_location == DIRECTLY_ABOVE:
            self.rect[0] = size[0] / 2 - self.image.get_size()[0] / 2
            self.rect[1] = 0
        elif self.GUI_location == UPPER_RIGHT:
            self.rect[0] = 0
            self.rect[1] = 0
        elif self.GUI_location == LOWER_RIGHT:
            self.rect[0] = 0
            self.rect[1] = size[1] - self.image.get_size()[1]
        elif self.GUI_location == UPPER_LEFT:
            self.rect[0] = size[0] - self.image.get_size()[0]
            self.rect[1] = 0
        elif self.GUI_location == LOWER_LEFT:
            self.rect[0] = size[0] - self.image.get_size()[0]
            self.rect[1] = size[1] - self.image.get_size()[1]
        if offset is not None:
            self.rect[0] += offset[0]
            self.rect[1] += offset[1]


CENTER = "CENTER"
DIRECTLY_ABOVE = "DIRECTLY_ABOVE"
DIRECTLY_BELOW = "DIRECTLY_BELOW"
UPPER_LEFT = "UPPER_LEFT"
LOWER_LEFT = "LOWER_LEFT"
UPPER_RIGHT = "UPPER_RIGHT"
LOWER_RIGHT = "LOWER_RIGHT"
