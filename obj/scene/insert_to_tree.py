from .Scene import Scene
import copy


def insert_to_tree(target: Scene, obj: Scene, index: int):
    target.tree.insert(index, copy.copy(obj))
