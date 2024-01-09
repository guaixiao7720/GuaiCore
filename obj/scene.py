import pygame
import copy


class Scene(pygame.sprite.Sprite):
    def __init__(self, game, name: str, models: dict = None, model: str or int = None):
        super().__init__()
        self.image = None

        # 场景的造型字典
        if models is not None:
            self.models = copy.deepcopy(models)
            self.models_bac = copy.deepcopy(models)

        # 属性
        self.name = name
        self.view = False
        self.is_running = True
        self.parent_scene = None

        # self.model 是 当前的造型 pygame.Surface self.models 是 造型字典
        # model 参数 是 当前造型 在 造型字典中的键值
        if models is not None:
            self.image = self.models[model]
            self.image_name = model
            self.rect = self.image.get_rect()
            self.rect.move((0, 0))
        else:
            self.image = None
            self.image_name = None

        # 场景树列表
        self.tree = []

        # 游戏对象的指针
        self.game = game


    def run(self):
        i = 0
        while i < len(self.tree):
            if self.tree[i].is_running:
                try:
                    self.tree[i].run()
                    self.tree[i].sprite_run()
                    self.tree[i].script()
                except AttributeError:
                    pass
                i += 1

    def draw(self):
        if self.image is not None:
            if self.parent_scene is None:
                self.game.screen.blit(self.image, self.rect)
            else:
                self.parent_scene.image.blit(self.image, self.rect)

        i = 0
        while i < len(self.tree):
            if self.tree[i].view:
                self.tree[i].draw()
                i += 1

    def set_models(self, models: dict or pygame.Surface, name: str = None):
        """
        设置该精灵的造型字典 或 某一项造型
        :param models: 造型 或 造型字典
        :param name:
        :return:
        """
        if isinstance(models, dict):
            self.models = copy.deepcopy(models)
            self.models_bac = copy.deepcopy(models)
        elif isinstance(models, pygame.Surface) and name is not None:
            self.models[name] = copy.deepcopy(models)
            self.models_bac[name] = copy.deepcopy(models)

    def set_image(self, name):
        self.image = self.models[name]
        self.image_name = name

    def when_window_resize_run(self):
        i = 0
        while i < len(self.tree):
            if self.tree[i].is_running:
                try:
                    self.tree[i].when_window_resize_run()
                except AttributeError:
                    pass
                i += 1


    def hidden(self):
        self.view = False

    def show(self):
        self.view = True

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

    def set_parent_scene(self, parent_scene):
        # 指针
        self.parent_scene = copy.deepcopy(parent_scene)


def add_to_tree(target: Scene, obj: Scene):
    target.tree.append(copy.copy(obj))


def insert_to_tree(target: Scene, obj: Scene, index: int):
    target.tree.insert(index, copy.copy(obj))


def delete_from_tree(target: Scene, index: int, obj: Scene = None):
    """
    删除或替换目标场景树中的索引项
    :param target: 目标场景
    :param index: 索引
    :param obj: 可选，当选择时，替换目标场景书中的索引项
    :return: 无
    """
    if obj is None:
        del target.tree[index]
    else:
        target.tree[index] = copy.copy(obj)
