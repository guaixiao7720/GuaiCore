import pygame

import Obj.GUI


class BackGround(Obj.GUI.GUI):
    def __init__(self, game, name, models, model):
        super().__init__(game, name, models, model)
        self.GUI_location = Obj.GUI.CENTER

    def when_window_resize_run(self):
        self.reset_background_size()
        self.set_location()

    def reset_background_size(self):
        for key in self.models.keys():
            image_size = self.models[key].get_size()
            if image_size[1] > pygame.display.get_window_size()[1]:
                size = pygame.display.get_window_size()[1]
                scale = image_size[1] / size
                # 获得相应等比例的图像宽度。
                width_size = int(image_size[0] / scale)
                self.image = pygame.transform.scale(self.models_bac[self.image_name], (width_size, size))
                self.set_location(Obj.GUI.CENTER)

        image_size = self.image.get_size()

        if image_size[1] > pygame.display.get_window_size()[1]:
            size = pygame.display.get_window_size()[1]
            scale = image_size[1] / size
            # 获得相应等比例的图像宽度。
            width_size = int(image_size[0] / scale)
            self.image = pygame.transform.scale(self.models_bac[self.image_name], (width_size, size))
            self.set_location(Obj.GUI.CENTER)
