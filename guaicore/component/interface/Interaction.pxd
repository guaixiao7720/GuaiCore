

cdef class Interaction:
    cdef public bint is_clicked_rect(self, int butt)
    cdef public bint is_clicked_mask(self, int butt)