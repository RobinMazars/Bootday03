import numpy as np


class ScrapBooker(object):
    """docstring for ScrapBooker."""

    def __init__(self):
        pass

    def crop(self, array, dimensions, position=(0, 0)):
        if dimensions[0] > array.shape[0] or dimensions[1] > array.shape[1]:
            raise ValueError(
                f"Dimension too high {dimensions[0]} > {array.shape[0]}"
                + f" or {dimensions[1]} > {array.shape[1]} ")
        fi = array[position[0]:dimensions[0], position[1]:dimensions[1]]
        return fi

    def juxtapose(self, array, n, axis):
        start = array
        for x in range(n-1):
            array = np.concatenate((array, start), axis)
        return array

    def thin(self, array, n, axis):
        if axis == 0:
            return np.delete(array, slice(n-1, None, n), 1)
        elif axis == 1:
            return np.delete(array, slice(n-1, None, n), 0)

    def mosaic(self, array, dimensions):
        return np.tile(array, dimensions + (1,))


def char_range(c1, c2):
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


sb = ScrapBooker()


finarr = []
arr = list("ABCD")
for x in arr:
    finarr.append(arr)
img = np.array(finarr)
img = img.T
print(img)

print("crop")
cr = sb.crop(img, (img.shape[0]//2, img.shape[1]//2), (0, 0))
print(cr)

print("jux")
ju = sb.juxtapose(img, 2, 0)
print(ju)

print("mosaic")
mo = sb.mosaic(img, (1, 2))
print(mo)

print("thin")
mo = sb.thin(img, 3, 0)
print(mo)
