from ImageProcessor import ImageProcessor
import numpy as np


class ColorFilter(object):
    """docstring for ColorFilter."""

    def __init__(self):
        pass

    def invert(self, arg):
        for x in arg:
            for y in x:
                y[0] = 1 - y[0]
                y[1] = 1 - y[1]
                y[2] = 1 - y[2]
        return arg

    def to_blue(self, arg):
        for x in arg:
            for y in x:
                y[0] = 0
                y[1] = 0
        return arg

    def to_green(self, arg):
        for x in arg:
            for y in x:
                y[0] = 0 * y[0]
                y[2] = 0 * y[0]
        return arg

    def to_red(self, arg):
        for x in arg:
            for y in x:
                y[1] = y[1] - y[1]
                y[2] = y[2] - y[2]
        return arg

    def getcolor(self, color, threshold):
        for x in np.linspace(1, 0, threshold+1):
            if color > x:
                return x

    def celluloid(self, arg, threshold=4):
        for x in arg:
            for y in x:

                y[0] = self.getcolor(y[0], threshold)
                y[1] = self.getcolor(y[1], threshold)
                y[2] = self.getcolor(y[2], threshold)
        return arg

    def to_grayscale(self, arg, filter="weighted"):
        if not isinstance(filter, str):
            raise TypeError("Bad type for filter")
        if filter == "weighted" or filter == "w":
            for x in arg:
                for y in x:
                    y[0] = 0.299 * y[0]
                    y[1] = 0.587 * y[1]
                    y[2] = 0.114 * y[2]
            return arg
        elif filter == "mean" or filter == "m":
            for x in arg:
                for y in x:
                    m = y[:2].sum()/3
                    y[0] = m
                    y[1] = m
                    y[2] = m
            return arg


imp = ImageProcessor()
img = imp.load("elon.png")
cf = ColorFilter()

fi = cf.invert(img)
# fi = cf.to_red(img)
# fi = cf.to_blue(img)
# fi = cf.to_green(img)
# fi = cf.celluloid(img)
# fi = cf.to_grayscale(img, "w")
# fi = cf.to_grayscale(img, "m")

imp.display(fi)
