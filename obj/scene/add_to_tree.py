from .Scene import Scene
import copy


def add_to_tree(target, obj):
    try:
        if target._has_camera:
            obj._has_camera = True
    except AttributeError:
        pass
    target.tree.append(obj)
