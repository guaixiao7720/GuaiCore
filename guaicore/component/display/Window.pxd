cdef class Window:
    cdef public bint __is_window
    cdef public bint drag
    cdef public bint scroll_vertically
    cdef public bint scroll_horizontal
    cdef bint __is_scrolling
    cdef float __sensitivity
    cdef int[2] first_pos
    cdef int[2] second_pos


    cdef public void window_init(self)
    cdef public void window_run(self)
    cdef public void set_window_size(self, new_size: list[int or float] or tuple[int or float])
    cdef void __tree_position_precent(self, tree: list)
    cdef void __tree_size_precent(self, tree: list, window_new_size: list[int or float] or tuple[int or float])
    cdef void __tree_scroll_vertically(self, tree: list, float num)
    cdef void __tree_scroll_horizontal(self, tree: list, float num)
    cdef void __scroll_run(self)
    cdef void __drag_run(self)
