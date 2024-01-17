from .Scene import Scene
import copy


def add_to_tree(target, obj):
    obj.parent_scene = target
    target.tree.append(obj)
