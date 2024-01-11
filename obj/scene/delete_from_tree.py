from .Scene import *


def delete_from_tree(target: Scene, index: int, obj: Scene = None):
    """
    删除或替换目标场景树中的索引项
    :param target: 目标场景
    :param index: 索引
    :param obj: 可选，当选择时，替换目标场景书中的索引项
    :return: 无
    """
    if obj is None:
        del target.tree[index]
    else:
        target.tree[index] = copy.copy(obj)
