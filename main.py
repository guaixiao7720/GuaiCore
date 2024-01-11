import os
import pygame

import obj
import Game

if __name__ == "__main__":
    pygame.init()


    class test(obj.BackGround.BackGround, obj.interface.Interaction.Interaction):
        def __init__(self, game):
            super().__init__(game, "测试", {1: pygame.image.load(PATH + "test_bg.png")}, 1)

        def script(self):
            # print("running")
            if self.is_clicked(0):
                print("被点击")



    class test2(obj.Sprite.Sprite):
        def __init__(self, game):
            super().__init__(game, "测试2", {1: pygame.image.load(PATH + "box2.png")}, 1)

        def script(self):
            if pygame.key.get_pressed()[pygame.K_w]:
                self.rect[1] -= 1
            if pygame.key.get_pressed()[pygame.K_s]:
                self.rect[1] += 1
            if pygame.key.get_pressed()[pygame.K_d]:
                self.rect[0] += 1
            if pygame.key.get_pressed()[pygame.K_a]:
                self.rect[0] -= 1

            if pygame.mouse.get_pressed(3)[0]:
                self.rect[0] = pygame.mouse.get_pos()[0]
                self.rect[1] = pygame.mouse.get_pos()[1]


    PATH = os.path.abspath(".") + "/"

    game = Game.new_game("Human", pygame.display.set_mode((1024,700), pygame.RESIZABLE))

    game.PATH = PATH

    cash = test(game)
    cash.reset_background_size()
    cash.show()
    cash.start()
    obj.scene.add_to_tree(game.main_scene, cash)

    cash2 = test2(game)
    cash2.show()
    cash2.run()
    obj.scene.add_to_tree((game.main_scene.tree[0]), cash2)

    cach = obj.GUI.GUI(game, "测试场景", {"哈哈哈": pygame.image.load(PATH + "box2.png")}, "哈哈哈")
    cach.set_location(obj.GUI.DIRECTLY_BELOW)

    game.setting_dict["UI_scaling"] = -40
    cach.scale_run()

    cach.move_in_milliseconds((0, 0), 3000)

    cach.show()
    cach.start()

    obj.scene.add_to_tree(game.main_scene, cach)

    text1 = obj.Text.Text(game, "111", "你好", 20)

    text1.set_text("你好", 20, False, (0, 0, 0), text1.rect)
    text1.set_location(obj.GUI.CENTER)
    text1.show()
    text1.start()
    obj.scene.add_to_tree(game.main_scene, text1)

    input1 = obj.TextInput.Textinput(game, 150, 40, 15, 15)
    input1.view = True
    obj.scene.add_to_tree(game.main_scene, input1)


    game.start()
