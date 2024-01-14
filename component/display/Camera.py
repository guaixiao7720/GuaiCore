import pygame


class Camera:
    def camera_init(self):
        self.camera_position = [0, 0]
        self.position = [0, 0]
        self.__has_camera = True

    def camera_draw(self):
        self.rect[0] = self.position[0] + self.camera_position[0]
        self.rect[1] = self.position[1] + self.camera_position[1]
        self.__tree_camera_draw(self.tree)

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

    def __tree_camera_draw(self, tree: list):
        for key in tree:
            key.rect[0] = key.position[0] + self.camera_position[0]
            key.rect[1] = key.position[1] + self.camera_position[1]
            key._has_camera = True
            if len(key.tree) > 0:
                self.__tree_camera_draw(key.tree)
