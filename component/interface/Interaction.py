import pygame

from obj.scene.Scene import Scene


class Interaction(Scene):
    def __init__(self, game, name: str, models: dict = None, model: str or int = None):
        super().__init__(game, name, models, model)
        self.text_input = None

    def is_clicked(self, num: int):
        mouse_pos_boolx = self.image.get_size()[0] + self.rect[0] > pygame.mouse.get_pos()[0] > self.rect[0]
        mouse_pos_booly = self.image.get_size()[1] + self.rect[1] > pygame.mouse.get_pos()[1] > self.rect[1]

        if self.game.event["MOUSEBUTTONDOWN"]  and pygame.mouse.get_pressed(5)[num] and mouse_pos_boolx and mouse_pos_booly:
            self.game.event["MOUSEBUTTONDOWN"] = False
            del mouse_pos_boolx, mouse_pos_booly
            return True
        else:
            del mouse_pos_boolx, mouse_pos_booly
            return False


    # SDL2 的附加功能未能正常调用 我也不知道为什么 只能暂时遗弃
    def start_textinput(self):
        pygame.key.start_text_input()
        pygame.key.set_text_input_rect(pygame.Rect(100,100,100,100))
        # 接口使用对象的 输入字符串
        self.text_input = self.game.event["TEXTINPUT"]

