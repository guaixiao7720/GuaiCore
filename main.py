import os
import pygame

import obj
import Game

if __name__ == "__main__":
    pygame.init()


    class test(obj.BackGround.BackGround, obj.Interface.Interaction.Interaction):
        def __init__(self, game):
            super().__init__(game, "测试", {1: pygame.image.load(PATH + "test_bg.png")}, 1)

        def script(self):
            # print("running")
            print(game.event["TEXTINPUT"])
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
    obj.Scene.add_to_tree(game.main_scene, cash)

    cash2 = test2(game)
    cash2.show()
    cash2.run()
    obj.Scene.add_to_tree((game.main_scene.tree[0]), cash2)

    cach = obj.GUI.GUI(game, "测试场景", {"哈哈哈": pygame.image.load(PATH + "box2.png")}, "哈哈哈")
    cach.set_location(obj.GUI.DIRECTLY_BELOW)

    game.setting_dict["UI_scaling"] = -40
    cach.scale_run()

    cach.show()
    cach.start()

    obj.Scene.add_to_tree(game.main_scene, cach)

    game.start()
