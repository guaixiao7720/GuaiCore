import threading
from . cimport Game
from . import Game
import pygame

cdef class SceneRun(threading.Thread):
    cdef Game.Game game
    cdef bint is_stop
    cdef pygame.Clock clock
    cdef public int run_speed
    cdef public str system_name

    cdef public void test_run(self)

