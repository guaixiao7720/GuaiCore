from .Scene import Scene
import copy


def add_to_tree(target: Scene, obj: Scene):
    target.tree.append(obj)
