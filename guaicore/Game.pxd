import pygame

from . import SceneRun

cdef class Game:
    cdef public str PATH
    cdef bint running
    cdef public pygame.surface.Surface screen
    cdef public str name
    cdef pygame.Clock Run_clock
    setting_dict: dict
    cdef public pygame.Color bg_color
    event: dict
    name_dict: dict
    FONT: dict[pygame.Font]
    cdef public  main_scene
    cdef SceneRun.SceneRun main_running

    cdef public void run(self)
    cdef void __event_manager(self)
cdef public Game new_game(str name, pygame.Surface screen)