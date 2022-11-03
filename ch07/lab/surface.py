from rectangle import rectangle

class surface:
    def __init__(self, filename, x, y, h, w):
        self.rect = rectangle(x,y,w,h)
        self.image = filename

    def getRect(self):
        return self.rect

        