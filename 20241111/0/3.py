class Rectangle():
    rectcnt = 0

    def __init__(self, x1, y1, x2, y2):
        self.__class__.rectcnt += 1
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        setattr(self, f"rect_{self.rectcnt}", self.rectcnt)

    def __str__(self):
        return f"{self.x1, self.y1}{self.x1, self.y2}{self.x2, self.y2}{self.x2, self.y1}"

tmp = Rectangle(1, 2, 3, 4)
tmp1 = Rectangle(0, 1, 2, 3)
tmp2 = Rectangle(5, 6, 7, 8)
print(dir(tmp2))