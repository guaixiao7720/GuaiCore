import os

import pygame

import Game
import obj
import component

if __name__ == "__main__":
    pygame.init()
    PATH = os.path.abspath(".") + "/"

    class test(obj.scene.Sprite, component.interface.Interaction, component.display.Window):
        def __init__(self, game):
            super().__init__(game, "测试", {1: pygame.image.load(PATH + "test_bg.png")}, 1)
            self.window_init()
            self.show()
            self.disable_mask()
            obj.scene.add_to_tree(game.main_scene, self)


        def script(self):
            if self.game.event["MOUSEWHEEL"]:
                pass
            if pygame.key.get_pressed()[pygame.K_w]:
                self.position[1] -= 1
            if pygame.key.get_pressed()[pygame.K_s]:
                self.position[1] += 1
            if pygame.key.get_pressed()[pygame.K_a]:
                self.position[0] -= 1
            if pygame.key.get_pressed()[pygame.K_d]:
                self.position[0] += 1

            if pygame.key.get_pressed()[pygame.K_i]:
                self.set_window_size((self.get_width() + 20,
                                      self.get_height() + 20))

            if pygame.key.get_pressed()[pygame.K_k]:
                self.set_window_size((self.get_width() - 20,
                                      self.get_height() - 20))

            self.window_run()

        def when_keyboard_pressed(self, key):
            # if key == pygame.K_w:
            #     self.position[1] -= 1
            # if key == pygame.K_s:
            #     self.position[1] += 1
            # if key == pygame.K_a:
            #     self.position[0] -= 1
            # if key == pygame.K_d:
            #     self.position[0] += 1
            # if key == pygame.K_i:
            #     pass
            # if key == pygame.K_k:
            #     pass
            pass




    class Sans(obj.scene.Sprite, component.interface.Interaction):
        def __init__(self, game):
            super().__init__(game, "sans", {1: pygame.image.load(f"{PATH}sans.png")}, 1)
            self.position = [250, 250]
            self.show()
            obj.scene.add_to_tree(cash, self)

        def script(self):
            # print(self.game.event_obj)
            if self.is_clicked_mask(0):
                print(1213)


    class test2(obj.scene.Sprite, component.interface.Interaction):
        def __init__(self, game):
            super().__init__(game, "测试2", {1: pygame.image.load(PATH + "box2.png")}, 1)

        def script(self):
            if pygame.key.get_pressed()[pygame.K_w]:
                self.rect[1] -= 0.2
            if pygame.key.get_pressed()[pygame.K_s]:
                self.rect[1] += 0.2
            if pygame.key.get_pressed()[pygame.K_d]:
                self.rect[0] += 0.2
            if pygame.key.get_pressed()[pygame.K_a]:
                self.rect[0] -= 0.2

            if pygame.mouse.get_pressed(3)[0]:
                self.rect[0] = pygame.mouse.get_pos()[0]
                self.rect[1] = pygame.mouse.get_pos()[1]




    game = Game.new_game("Human", pygame.display.set_mode((1024, 700), pygame.RESIZABLE))

    game.PATH = PATH

    cash = test(game)
    # cash.reset_background_size()
    cash.show()
    cash.start()
    obj.scene.add_to_tree(game.main_scene, cash)

    cash2 = test2(game)
    cash2.show()
    cash2.run()
    obj.scene.add_to_tree(cash, cash2)

    cach = obj.scene.gui.GUI(game, "测试场景", {"哈哈哈": pygame.image.load(PATH + "box2.png")}, "哈哈哈")
    cach.set_location(obj.scene.gui.DIRECTLY_BELOW)

    game.setting_dict["UI_scaling"] = -40
    cach.scale_run()



    cach.show()
    cach.start()

    # obj.scene.add_to_tree(cash, cach)

    text1 = obj.scene.gui.Text(game, "111", "你好", 20)

    text1.set_text("你好", 20, False, (0, 0, 0), text1.rect)
    text1.set_location(obj.scene.gui.CENTER)
    text1.show()
    text1.start()

    input1 = obj.scene.textInput.TextInput.Textinput(game, "测试输入框", 150, 40, 15, 15)
    input1.show()
    obj.scene.add_to_tree(cash, input1)

    obj.get_obj_from_name(game.name_dict, "测试2").hide()
    obj.get_obj_from_name(game.name_dict, "测试2").stop()

    bgm = obj.sound.Music(game, "TOBY", {"1" : pygame.mixer.Sound(PATH+"Bring_it_in.ogg")}, "1")

    bgm.play_start(5)

    sans = Sans(game)
    sans.hide()

    gezi1 = obj.scene.Sprite(game, "gezi1", {1: pygame.image.load(PATH + "box2.png")}, 1)
    gezi1.show()
    gezi1.position = [700, 150]

    obj.scene.add_to_tree(obj.get_obj_from_name(game.name_dict, "测试"), gezi1)

    gezi2 = obj.scene.Sprite(game, "gezi2", {1: pygame.image.load(PATH + "box2.png")}, 1)
    gezi2.show()
    gezi2.position = [gezi1.rect[2] + 700, 150]

    obj.scene.add_to_tree(obj.get_obj_from_name(game.name_dict, "测试"), gezi2)
    game.start()

