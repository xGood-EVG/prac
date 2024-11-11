class Rectangle():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def __str__(self):
        return f"{self.x1, self.y1}{self.x1, self.y2}{self.x2, self.y2}{self.x2, self.y1}"

tmp = Rectangle(1, 2, 3, 4)
print(tmp)