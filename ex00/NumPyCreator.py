import numpy as np


class NumPyCreator(object):
    """docstring for NumPyCreator."""

    def __init__(self):
        pass

    def from_list(self, lst):
        return np.array(lst)

    def from_tuple(self, lst):
        return np.array(lst)

    def from_iterable(self, lst):
        return np.array(lst)

    def from_shape(self, sha, value=0):
        return np.full(sha, value)

    def random(self, sha):
        rng = np.random.default_rng()
        return rng.random(sha)

    def identity(self, lst):
        return np.identity(lst)


npc = NumPyCreator()
print(npc.from_list([1, 2, 3]))
print(npc.from_tuple((1, 2, 3)))
print(npc.from_iterable(range(1, 20)))
shape = (3, 5)
print(npc.from_shape(shape, 1))
print(npc.random(shape))
print(npc.identity(4))
