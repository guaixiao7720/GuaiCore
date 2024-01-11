from .Scene import *


def add_to_tree(target: Scene, obj: Scene):
    target.tree.append(copy.copy(obj))
