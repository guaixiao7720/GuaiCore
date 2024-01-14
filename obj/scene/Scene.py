import pygame
import copy

from obj.Obj import Obj


class Scene(Obj):
    def __init__(self, game, name: str, models: dict = None, model: str or int = None):
        super().__init__(game, name)
        self._has_camera = False
        self._alpha = None
        self.__is_changed = False
        self.image = None
        self.position = [0, 0]

        # 场景的造型字典
        if models is not None:
            self.models = copy.deepcopy(models)
        # 属性

        self.__view = False
        self.parent_scene = None


        # self.model 是 当前的造型 pygame.Surface self.models 是 造型字典
        # model 参数 是 当前造型 在 造型字典中的键值
        if models is not None:
            self.image = self.models[model]
            self.__image_bac = copy.copy(self.image)
            self.rect = self.image.get_rect()
            self.rect.move((0, 0))
            self.__width = self.rect[2]
            self.__height = self.rect[3]
        else:
            self.image = None
            self.__image_bac = None
            self.__width = 0
            self.__height = 0

        if model is None:
            self.mask = None
        else:
            self.mask = pygame.mask.from_surface(self.image)

        # 场景树列表
        self.tree = []

    def run(self):

        if self.__is_changed and self.image is not None:
            new_image = pygame.transform.smoothscale(self.__image_bac, (self.__width, self.__height))
            new_image.set_alpha(self._alpha)
            self.image = copy.copy(new_image)
            del new_image

            self.__is_changed = False

            try:
                self.change_mask_from_image()
            except AttributeError:
                pass

        i = 0
        while i < len(self.tree):
            if self.tree[i].get_running():
                try:
                    self.tree[i].run()
                    try:
                        self.tree[i].sprite_run()
                    except AttributeError:
                        pass
                    try:
                        self.tree[i].script()
                    except AttributeError:
                        pass
                except AttributeError:
                    pass
            i += 1

    def draw(self):
        if self.image is not None:
            if not self._has_camera:
                self.rect[0] = self.position[0]
                self.rect[1] = self.position[1]

            if self.parent_scene is None:
                self.game.screen.blit(self.image, self.rect)
            else:
                self.parent_scene.image.blit(self.image, self.rect)
        i = 0
        while i < len(self.tree):

            try:
                if self.tree[i].get_view():
                    try:
                        self.tree[i].camera_draw()
                    except:
                        pass
                    self.tree[i].draw()
            except AttributeError:
                i += 1
                continue
            i += 1

    def event_run(self):
        i = 0
        while i < len(self.tree):
            if self.tree[i].get_running():
                try:
                    self.tree[i].event_run()
                except AttributeError:
                    pass
            i += 1

    def set_models(self, models: dict or pygame.Surface, name: str = None):
        """
        设置该精灵的造型字典 或 某一项造型
        :param models: 造型 或 造型字典
        :param name: models字典键值
        :return:
        """
        if isinstance(models, dict):
            self.models = copy.deepcopy(models)

        elif isinstance(models, pygame.Surface) and name is not None:
            self.models[name] = copy.deepcopy(models)

        self.__is_changed = True

    def set_image(self, name):
        self.image = self.models[name]
        self.image_name = name
        self.__is_changed = True

    def when_window_resize_run(self):
        i = 0
        while i < len(self.tree):
            if self.tree[i].get_running():
                try:
                    self.tree[i].when_window_resize_run()
                except AttributeError:
                    pass
            i += 1
        self.__is_changed = True

    def hide(self):
        self.__view = False

    def show(self):
        self.__view = True

    def get_view(self):
        return self.__view

    def set_parent_scene(self, parent_scene):
        # 指针
        self.parent_scene = copy.deepcopy(parent_scene)

    def change_mask_from_image(self):
        self.mask = pygame.mask.from_surface(self.image)

    def set_position(self, posit : list or tuple):
        self.rect[0] = posit[0]
        self.rect[1] = posit[1]
        self.position = posit

    def set_width(self, num):
        self.__is_changed = True
        self.__width = num
        self.rect[2] = self.__width

    def get_width(self):
        return self.__width

    def set_height(self, num):
        self.__is_changed = True
        self.__height = num
        self.rect[3] = self.__height

    def get_height(self):
        return self.__height
