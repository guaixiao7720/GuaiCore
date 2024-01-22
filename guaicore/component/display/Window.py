import copy

import pygame

from ...obj import get_obj_from_name


class Window:

    def window_init(self, scroll_vertical: bool = False, scroll_horizontal: bool = False, sensitivity: int = 100, drag: bool = False):
        self._is_window = True

        # 窗口是否支持拖动
        self.drag = False

        # 该 window 组件是否支持垂直滚动
        self.scroll_vertically = scroll_vertical
        # 该 window 组件是否支持横向滚动
        self.scroll_horizontal = scroll_horizontal

        if self.scroll_vertically or self.scroll_horizontal:
            self.__is_scrolling = False
            self.first_pos = (0, 0)
            self.second_pos = (0, 0)

            # 灵敏度 百分比修正
            self.__sensitivity = sensitivity / 100
        else:
            self.__is_scrolling = False
            self.first_pos = (0, 0)
            self.second_pos = (0, 0)

            # 灵敏度 百分比修正
            self.__sensitivity = sensitivity / 100

            self.drag = drag

    def window_run(self):
        if self.scroll_vertically or self.scroll_horizontal:
            self.__scroll_run()
        elif self.drag:
            self.__drag_run()

        self.__tree_position_precent(self.tree)

    def set_window_size(self, new_size: list or tuple[int]):
        self.__tree_size_precent(self.tree, new_size)

        self._image_cache = copy.deepcopy(self.image)

        self.position[0] += self.get_width() - new_size[0]
        self.position[1] += self.get_height() - new_size[1]

        self.set_width(new_size[0])
        self.set_height(new_size[1])

        self._is_changed = True


    def __tree_position_precent(self, tree: list):
        for key in tree:
            key.rect[0] = int(self.position[0] + key.position[0])
            key.rect[1] = int(self.position[1] + key.position[1])

            if len(key.tree) > 0:
                self.__tree_position_precent(key.tree)

    def __tree_size_precent(self, tree: list, window_new_size: tuple or list[int]):
        for key in tree:
            try:
                if key.image is not None:
                    key._is_changed = True
                    width_precent = key.get_width() / self.get_width()
                    height_precent = key.get_height() / self.get_height()
                    x_precent = abs((key.position[0]) / self.get_width())
                    y_precent = abs((key.position[1]) / self.get_height())

                    key.set_width(window_new_size[0] * width_precent)
                    key.set_height(window_new_size[1] * height_precent)

                    key.position[0] = window_new_size[0] * x_precent
                    key.position[1] = window_new_size[1] * y_precent



            except AttributeError:
                pass
            finally:

                if len(key.tree) > 0:
                    self.__tree_size_precent(key.tree, window_new_size)

    def __tree_scroll_vertically(self, tree: list, num: float):
        for key in tree:
            key.position[1] += num
            if len(key.tree) > 0:
                self.__tree_position_precent(key.tree)

    def __tree_scroll_horizontal(self, tree: list, num: float):
        for key in tree:
            key.position[0] += num
            if len(key.tree) > 0:
                self.__tree_position_precent(key.tree)


    def __scroll_run(self):

        if not self.__is_scrolling:

            if pygame.sprite.collide_rect(self, get_obj_from_name(self.game.name_dict, "mouse")) and pygame.mouse.get_pressed(3)[0]:
                self.first_pos = pygame.mouse.get_pos()
                self.__is_scrolling = True


        else:
            if pygame.mouse.get_pressed(3)[0] and pygame.sprite.collide_rect(self, get_obj_from_name(self.game.name_dict, "mouse")):
                self.second_pos = pygame.mouse.get_pos()
                if self.scroll_vertically:
                    self.__tree_scroll_vertically(self.tree, (int(self.second_pos[1] - self.first_pos[1]) * self.__sensitivity))
                if self.scroll_horizontal:
                    self.__tree_scroll_horizontal(self.tree, (int(self.second_pos[0] - self.first_pos[0]) * self.__sensitivity))
                self.first_pos = pygame.mouse.get_pos()
            else:
                self.__is_scrolling = False

    def __drag_run(self):

        if not self.__is_scrolling:

            if pygame.sprite.collide_rect(self, get_obj_from_name(self.game.name_dict, "mouse")) and pygame.mouse.get_pressed(3)[0]:
                self.first_pos = pygame.mouse.get_pos()
                self.__is_scrolling = True


        else:
            if pygame.mouse.get_pressed(3)[0] and pygame.sprite.collide_rect(self, get_obj_from_name(self.game.name_dict, "mouse")):
                self.second_pos = pygame.mouse.get_pos()
                self.position[0] += (self.second_pos[0] - self.first_pos[0]) * self.__sensitivity
                self.position[1] += (self.second_pos[1] - self.first_pos[1]) * self.__sensitivity

                self.first_pos = pygame.mouse.get_pos()
            else:
                self.__is_scrolling = False













    # 傻逼垃圾屎山代码 重写啊啊啊啊啊啊啊啊啊啊啊

    # def camera_init(self):
    #     self.camera_position = [0, 0]
    #     self.position = [0, 0]
    #     self._has_camera = True
    #
    #     # 各子节点在地图中的占比位置
    #     self.position_percent = {}
    #
    #     ## 摄像机高度
    #     self._camera_high = 0
    #
    # def camera_draw(self):
    #
    #     if self.image is not None:
    #
    #         if self.parent_scene is None:
    #             self.game.screen.blit(self.image, (self.rect[0], self.rect[1]))
    #
    #         else:
    #             self.parent_scene.image.blit(self.image, (self.rect[0], self.rect[1]))
    #
    #     i = 0
    #     while i < len(self.tree):
    #
    #         try:
    #             if self.tree[i].get_view():
    #                 self.tree[i].draw()
    #         except AttributeError:
    #             i += 1
    #             continue
    #         i += 1
    #
    # def camera_run(self):
    #     self.rect[0] = self.position[0] + self.camera_position[0]
    #     self.rect[1] = self.position[1] + self.camera_position[1]
    #     self.__tree_camera_draw(self.tree)
    #
    #
    # def set_camera_high(self, num: int):
    #     self.set_width(num)
    #     self.set_height(num)
    #
    #     self.__tree_camera_high(self.tree, num)
    #
    #     # 修正scene位置
    #     self.position[0] += num
    #     self.position[1] += num
    #
    # def __tree_camera_draw(self, tree: list):
    #     for key in tree:
    #         key.rect[0] = key.position[0] + self.camera_position[0]
    #         key.rect[1] = key.position[1] + self.camera_position[1]
    #         # key._has_camera = True
    #         if len(key.tree) > 0:
    #             self.__tree_camera_draw(key.tree)
    #
    #
    #
    # def __tree_position_precent(self, tree: list, num: int or float):
    #     for key in tree:
    #         # key.set_width(key.get_width() + num)
    #         # key.set_height(key.get_height() + num)
    #         key_width_precent = key.get_width() / self.get_width()
    #         key_height_precent = key.get_height() / self.get_height()
    #         key_x_precent = key.position[0] // self.get_width() + self.position[0]
    #         key_y_precent = key.position[0] // self.get_height() + self.position[1]
    #         old_scene_width = self.get_width()
    #         old_scene_height = self.get_height()
    #
    #         # 设置scene大小
    #         self.set_width(num)
    #         self.set_height(num)
    #
    #
    #         # 修正子场景的大小和位置
    #         key.set_width(int(key_width_precent * key.get_width()))
    #         key.set_height(int(key_height_precent * key.get_height()))
    #
    #         key.position[0] = int((old_scene_width - num) * key_x_precent)
    #         key.position[1] = int((old_scene_height - num) * key_y_precent)
    #         key._is_changed = True
    #
    #
    #         # if key.position[1] >= self.__center_height:
    #         #     key.position[1] -= num
    #         # else:
    #         #     key.position[1] += num
    #
    #         # key._has_camera = True
    #         if len(key.tree) > 0:
    #             self.__tree_position_precent(key.tree, num)
    #
    pass
