import pygame


class Camera:
    def camera_init(self):
        self.camera_position = [0, 0]
        self.position = [0, 0]
        self.__has_camera = True

        ## 摄像机高度
        self._camera_high = 0

    def camera_draw(self):

        if self.image is not None:

            if self.parent_scene is None:
                self.game.screen.blit(self.image, (self.rect[0], self.rect[1]))

            else:
                self.parent_scene.image.blit(self.image, (self.rect[0], self.rect[1]))

        i = 0
        while i < len(self.tree):

            try:
                if self.tree[i].get_view():
                    self.tree[i].draw()
            except AttributeError:
                i += 1
                continue
            i += 1

    def camera_run(self):
        self.rect[0] = self.position[0] + self.camera_position[0]
        self.rect[1] = self.position[1] + self.camera_position[1]
        self.__tree_camera_draw(self.tree)


    def set_camera_high(self, num: int):
        self._camera_high += num
        self.__tree_camera_high(self.tree, num)

    def __tree_camera_draw(self, tree: list):
        for key in tree:
            key.rect[0] = key.position[0] + self.camera_position[0]
            key.rect[1] = key.position[1] + self.camera_position[1]
            key._has_camera = True
            if len(key.tree) > 0:
                self.__tree_camera_draw(key.tree)

    def __tree_camera_high(self, tree: list, num: int):
        for key in tree:
            key.set_width(key.get_width() + num)
            key.set_height(key.get_height() + num)
            key._has_camera = True
            if len(key.tree) > 0:
                self.__tree_camera_draw(key.tree)
