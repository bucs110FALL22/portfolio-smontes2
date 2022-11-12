class rectangle:

    def __init__(self, x, y, h, w):
        self.x = max(0,x)
        self.y = max(0,y)
        self.height = max(0,h)
        self.width = max(0,w) 
        
    def __str__(self):
        return f"(x:{self.x},y:{self.y})height: {self.height}, width:{self.width}"

"def __str__ returns a string containing the x, y, width, and height of the rectangle."
"returns the string coordinates"