from obj.rectangle import rectangle
from obj.border import border
import pygame
import os


def find_closest_number(num, lst):
    if len(lst):
        closest_num = lst[0]  # 将第一个数字设为初始的最接近数字

        for n in lst:
            if abs(num - n) < abs(num - closest_num):
                closest_num = n

        return closest_num
    return -1


class Textinput:
    os.environ["SDL_IME_SHOW_UI"] = "1"

    def __init__(self, game, width, height, x, y):
        self.game = game
        self.text = ""
        self.buf_text = ""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_running = True
        self.view = False
        self.rect = rectangle(self.game.screen, width + 5, height, x, y, background_color=(255, 255, 255),
                              rect_border=border(1, (0, 0, 0)))
        self.last_input_word = None
        self.font = self.game.FONT
        self.active = False
        point = self.rect.get_coordinate()
        pygame.key.set_text_input_rect((point.left, point.top + 10, point.width, point.height))
        pygame.key.stop_text_input()
        self.cursor = -1

    def draw(self):
        self.rect.draw()
        if self.active:
            font_range = self.font.size(self.text)
            if font_range[0] <= self.width:
                rect = self.rect.get_coordinate()
                self.buf_text = self.text
                self.game.screen.blit(self.font.render(self.text, True, (0, 0, 0)),
                                 (rect.x, rect.y + (self.height / 2 - self.font.get_height() / 2)))
            else:
                res = 0
                while True:
                    if self.font.size(self.text[res::])[0] <= self.width:
                        rect = self.rect.get_coordinate()
                        self.buf_text = self.text[res::]
                        self.game.screen.blit(self.font.render(self.text[res::], True, (0, 0, 0)),
                                         (rect.x, rect.y + (self.height / 2 - self.font.get_height() / 2)))
                        break
                    res += 1
            if self.cursor == -1:
                font_size = self.font.size(self.text)
                y_start = self.y + 3
                y_end = self.y + self.height - 3
                if font_size[0] <= self.width:
                    x = self.x + font_size[0] + 2
                    pygame.draw.line(self.game.screen, (0, 0, 0), (x, y_start), (x, y_end))
                else:
                    x = self.width + 2 + self.x
                    pygame.draw.line(self.game.screen, (0, 0, 0), (x, y_start), (x, y_end))
            else:
                y_start = self.y + 3
                y_end = self.y + self.height - 3
                x = self.font.size(self.buf_text[0:self.cursor])[0] + self.x
                pygame.draw.line(self.game.screen, (0, 0, 0), (x, y_start), (x, y_end))
        else:
            font_range = self.font.size(self.text)
            if font_range[0] <= self.width:
                rect = self.rect.get_coordinate()
                self.buf_text = self.text
                self.game.screen.blit(self.font.render(self.text, True, (0, 0, 0)),
                                 (rect.x, rect.y + (self.height / 2 - self.font.get_height() / 2)))
            else:
                res = 0
                while True:
                    if self.font.size(self.text[res::])[0] <= self.width:
                        rect = self.rect.get_coordinate()
                        self.buf_text = self.text[res::]
                        self.game.screen.blit(self.font.render(self.text[res::], True, (0, 0, 0)),
                                         (rect.x, rect.y + (self.height / 2 - self.font.get_height() / 2)))
                        break
                    res += 1

    def event_run(self):
        self.rect.handel(self.game.event_obj)
        if self.game.event_obj.type == pygame.MOUSEBUTTONDOWN:
            if self.game.event_obj.button == 1:
                if self.rect.is_clicked(pygame.mouse.get_pos()):
                    self.active = True
                    self.game.event["TEXTINPUT"] = True
                    pygame.key.start_text_input()
                    self.rect.border.color = self.rect.click_border_color
                    point = pygame.mouse.get_pos()
                    x_point = point[0] - self.x
                    x = [self.font.size(self.buf_text[:x])[0] for x in range(len(self.buf_text))]
                    n = find_closest_number(x_point, x)
                    try:
                        if x_point > max(x):
                            self.cursor = -1
                        else:
                            self.cursor = x.index(n)
                    except ValueError:
                        self.cursor = -1
                else:
                    self.active = False
                    self.game.event["TEXTINPUT"] = False
                    self.rect.border.color = (0, 0, 0)
        if self.active:
            if self.game.event_obj.type == pygame.TEXTINPUT:
                if self.cursor == -1:
                    self.text += self.game.event_obj.text
                    point = self.rect.get_coordinate()
                    pygame.key.set_text_input_rect((point.left, point.top + 10, point.width, point.height))
                else:
                    self.text = self.text[0:self.cursor] + self.game.event_obj.text + self.text[self.cursor:]
            elif self.game.event_obj.type == pygame.KEYDOWN:
                if self.game.event_obj.key == pygame.K_BACKSPACE:  # 退格键
                    if self.cursor == -1:
                        self.text = self.text[:-1]
                    elif self.cursor == 0:
                        return
                    else:
                        self.text = self.text[:self.cursor-1] + self.text[self.cursor:]
                        self.cursor -= 1

    def get_text(self):
        return self.text

if __name__ == '__main__':
    pygame.init()
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    running = True
    inp = Textinput(screen, 200, 30, 20, 100)
    inp2 = Textinput(screen, 200, 30, 20, 200)
    while running:
        screen.fill((0, 0, 0))

        for self.game.event_obj in pygame.self.game.event_obj.get():
            if self.game.event_obj.type == pygame.QUIT:
                running = False
            inp.run(self.game.event_obj)
            inp2.run(self.game.event_obj)

        screen.fill((255, 255, 255))
        inp.draw()
        inp2.draw()
        pygame.display.flip()