import matplotlib.image as mpimg
import matplotlib.pyplot as plt


class ImageProcessor(object):
    """docstring for ImageProcessor."""

    def __init__(self):
        pass

    def load(self, path):
        img = mpimg.imread(path)
        print(img.shape[:2])
        return img

    def display(self, arr):
        plt.imshow(arr)
        plt.show()


ip = ImageProcessor()
img = ip.load("../elon.png")
print(img)
ip.display(img)
