import pygame

from .GUI import GUI, CENTER, DIRECTLY_BELOW, DIRECTLY_ABOVE, LOWER_LEFT, LOWER_RIGHT, UPPER_LEFT, UPPER_RIGHT


class BackGround(GUI):
    def __init__(self, game, name, models, model):
        super().__init__(game, name, models, model)
        self.GUI_location = CENTER

    def when_window_resize_run(self):
        self.reset_background_size()
        self.set_location()
        self.__is_changed = True

    def reset_background_size(self):

        image_size = (self.get_width(), self.get_height())

        if image_size[1] != pygame.display.get_window_size()[1]:
            size = pygame.display.get_window_size()[1]
            scale = image_size[1] / size
            # 获得相应等比例的图像宽度。
            width_size = int(image_size[0] / scale)
            self.set_width(width_size)
            self.set_height(size)
            self.__is_changed = True
            self.set_location(CENTER)


