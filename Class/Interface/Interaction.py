import pygame
import Class.Scene


class Interaction(Class.Scene.Scene):
    def is_clicked(self, num: int):
        mouse_pos_boolx = self.image.get_size()[0] + self.position[0] > pygame.mouse.get_pos()[0] > self.position[0]
        mouse_pos_booly = self.image.get_size()[1] + self.position[1] > pygame.mouse.get_pos()[1] > self.position[1]

        if self.game.event["MOUSEBUTTONDOWN"]  and pygame.mouse.get_pressed(5)[num] and mouse_pos_boolx and mouse_pos_booly:
            self.game.event["MOUSEBUTTONDOWN"] = False
            del mouse_pos_boolx, mouse_pos_booly
            return True
        else:
            del mouse_pos_boolx, mouse_pos_booly
            return False
