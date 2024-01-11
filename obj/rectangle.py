import pygame
from obj.border import border
 
 
class rectangle:
    def __init__(self, screen, width, height, x, y, background_color=None, rect_border=None, fix=False,
                 click_background_color=(255, 255, 255), click_border_color=(64, 160, 255)):
        self.width = width
        self.height = height
        self.screen = screen
        self.window_width = screen.get_width()
        self.window_height = screen.get_height()
        self.x = x
        self.y = y
        self.background_color = background_color if background_color is not None else (255, 255, 255)
        self.click_background_color = click_background_color
        self.click_border_color = click_border_color
        self.background = self.background_color
        self.border = rect_border if rect_border is not None else border(1, self.background_color)
        self.selected = False
        self.offset = False
        self.fix = fix
 
    def draw(self):
        pygame.draw.rect(self.screen, self.border.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.screen, self.background,
                         (self.x+self.border.thickness, self.y+self.border.thickness,
                          self.width-(self.border.thickness*2), self.height-(self.border.thickness*2)))
 
    def get_coordinate(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
 
    def set_coordinate(self, x, y):
        self.x = x
        self.y = y
        if x <= 0:
            self.x = 0
        if x >= self.window_width-self.width:
            self.x = self.window_width-self.width
        if y <= 0:
            self.y = 0
        if y >= self.window_height-self.height:
            self.y = self.window_height-self.height
 
    def is_clicked(self, mouse_pos):
        are = self.get_coordinate()
        if are.collidepoint(mouse_pos):
            return True
        else:
            return False
 
    def handel(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.is_clicked(pygame.mouse.get_pos()):
                self.selected = True
                self.background = self.click_background_color
                self.border.color = self.click_border_color
                if self.fix:
                    point = pygame.mouse.get_pos()
                    self.offset = (point[0]-self.x, point[1]-self.y)
 
        if event.type == pygame.MOUSEMOTION:
            if self.selected and self.fix:
                point = pygame.mouse.get_pos()
                self.set_coordinate(point[0]-self.offset[0], point[1]-self.offset[1])
 
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.selected = False
                self.background = self.background_color
 
 
if __name__ == '__main__':
    pygame.init()
    width = 800
    height = 600
    screen = pygame.display.set_mode((width, height))
    running = True
    rect = rectangle(screen, 100, 100, 0, 0, fix=True, rect_border=border(1, (0, 255, 0)),background_color=(255, 255, 255))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            rect.handel(event)
 
        screen.fill((255,255,255))
        rect.draw()
        pygame.display.flip()