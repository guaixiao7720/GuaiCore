import pygame
# pygame._sdl2 需要SDL2
import pygame._sdl2
class Touch():
    # 重写 GUI类 windows系统的 is_clicked 方法
    def is_clicked(self):
        # 算了先做别的吧 待续
        pygame._sdl2.touch.get_num_devices()
