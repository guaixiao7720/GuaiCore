import pygame

from guaicore.obj.scene.Scene import Scene
from ...obj import get_obj_from_name


class Interaction(Scene):
    def __init__(self, game, name: str, models: dict = None, model: str or int = None):
        super().__init__(game, name, models, model)
        self.text_input = None

    def is_clicked_rect(self, butt: int):
        if pygame.sprite.collide_rect(self, get_obj_from_name(self.game.name_dict, "mouse")):
            if pygame.mouse.get_pressed(5)[butt] and self.game.event["MOUSEBUTTONDOWN"]:
                self.game.event["MOUSEBUTTONDOWN"] = False
                return True
        return False

    def is_clicked_mask(self, butt: int):
        if pygame.sprite.collide_mask(self, get_obj_from_name(self.game.name_dict, "mouse")):
            if pygame.mouse.get_pressed(5)[butt] and self.game.event["MOUSEBUTTONDOWN"]:
                self.game.event["MOUSEBUTTONDOWN"] = False
                return True
        return False




    # SDL2 的附加功能未能正常调用 我也不知道为什么 只能暂时遗弃
    # def start_textinput(self):
    #     pygame.key.start_text_input()
    #     pygame.key.set_text_input_rect(pygame.Rect(100,100,100,100))
    #     # 接口使用对象的 输入字符串
    #     self.text_input = self.game.event["TEXTINPUT"]

