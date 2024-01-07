if __name__ == "__main__":
    import os

    import pygame

    import Class.Interface.Interaction
    import Class.Scene
    import Game
    import Class.Sprite

    pygame.init()

    class test(Class.Sprite.Sprite, Class.Interface.Interaction.Interaction):
        def __init__(self, game):
            super().__init__(game, "测试", {1: pygame.image.load(PATH + "test_bg.png")}, 1)

        def script(self):
            # print("running")
            if self.is_clicked(0):
                print("被点击")

    class test2(Class.Sprite.Sprite):
        def __init__(self, game):
            super().__init__(game, "测试2", {1: pygame.image.load(PATH + "box2.png")}, 1)

        def script(self):
            if pygame.key.get_pressed()[pygame.K_w]:
                self.position[1] -= 1
            if pygame.key.get_pressed()[pygame.K_s]:
                self.position[1] += 1
            if pygame.key.get_pressed()[pygame.K_d]:
                self.position[0] += 1
            if pygame.key.get_pressed()[pygame.K_a]:
                self.position[0] -= 1

            if pygame.mouse.get_pressed(3)[0]:
                self.position[0] = pygame.mouse.get_pos()[0]
                self.position[1] = pygame.mouse.get_pos()[1]

    PATH = os.path.abspath(".") + "/"

    game = Game.new_game("Human", pygame.display.set_mode((600,400)))

    game.PATH = PATH

    cash = test(game)
    cash.show()
    cash.start()
    Class.Scene.add_to_tree(game.main_scene, cash)

    cash2 = test2(game)
    cash2.show()
    cash2.run()
    Class.Scene.add_to_tree((game.main_scene.tree[0]) , cash2)


    cach = Class.Scene.Scene(game, "测试场景", {"哈哈哈": pygame.image.load(PATH + "box2.png")}, "哈哈哈")
    cach.show()
    cach.start()

    Class.Scene.add_to_tree(game.main_scene, cach)

    game.start()
