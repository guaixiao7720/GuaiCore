if __name__ == "__main__":
    import os

    import pygame

    import Class.Interface.Interaction
    import Class.Scene
    import Game
    import Class.Sprite

    pygame.init()


    # class Test(pygame.sprite.Sprite):
    #     def __init__(self):
    #         super().__init__()
    #         self.is_running = True
    #         self.view = True
    #
    #         self.image = pygame.image.load(PATH + "box2.png")
    #         self.rect = self.image.get_rect()
    #         self.position = [0, 0]
    #
    #     def run(self):
    #         if pygame.key.get_pressed()[pygame.K_w]:
    #             self.position[1] -= 1
    #         if pygame.key.get_pressed()[pygame.K_s]:
    #             self.position[1] += 1
    #         if pygame.key.get_pressed()[pygame.K_d]:
    #             self.position[0] += 1
    #         if pygame.key.get_pressed()[pygame.K_a]:
    #             self.position[0] -= 1
    #
    #         if pygame.mouse.get_pressed(num_buttons=3)[0]:
    #             self.position[0] = pygame.mouse.get_pos()[0]
    #             self.position[1] = pygame.mouse.get_pos()[1]
    #
    #     def draw(self):
    #         game.screen.blit(self.image, self.position)

    class test(Class.Sprite.Sprite, Class.Interface.Interaction.Interaction):
        def __init__(self, game):
            super().__init__(game, "测试", {1: pygame.image.load(PATH + "test_bg.png")}, 1)

        def script(self):
            # print("running")
            if self.is_clicked(0):
                print("被点击")

    PATH = os.path.abspath(".") + "/"

    game = Game.new_game("Human", pygame.display.set_mode((600,400)))

    game.PATH = PATH

    cash = test(game)
    cash.show()
    cash.start()
    Class.Scene.add_to_tree(game.main_scene, cash)

    cach = Class.Scene.Scene(game, "测试场景", {"哈哈哈": pygame.image.load(PATH + "box2.png")}, "哈哈哈")
    cach.show()
    cach.start()

    Class.Scene.add_to_tree(game.main_scene, cach)

    game.start()
