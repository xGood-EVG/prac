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
    
    def __abs__(self):
        return abs((self.x2 - self.x1) * (self.y2 - self.y1))
    
    def __lt__(self, other):
        return self.__abs__() < other.__abs__()
    
    def __eq__(self, other):
        return self.__abs__() == other.__abs__()
    
    def __mul__(self, num):
        return self.__class__(self.x1 * num, self.y1 * num, self.x2 * num, self.y2 * num)
    
    def __rmul__(self, num):
        return self.__mul__(num)
    
    def __getitem__(self, index):
        gtitm = [(self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1)]
        return gtitm[index]
    
    def __bool__(self):
        return self.__abs__() != 0
    
    def __del__(self):
        self.__class__.rectcnt -= 1
        print(self.rectcnt)

    def __iter__(self):    # Вместо getitem
        return iter(((self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1)))
    
t = Rectangle(5, 5, 5, 5)
s = Rectangle(0, 1, 2, 3)
r = Rectangle(5, 6, 7, 9)
o = Rectangle(1, 2, 3, 4)
print(*(f"{n}({bool(x)}):{round(abs(x), 3)}" for n, x in zip("rsto", (r, s, t, o))))
# print(tmp2[2])
# print(list(tmp1))
# print()
# for x, y in tmp2:
#     print(x, y)
# print()
# print(tmp1.__bool__())
# print()
# for i in Rectangle(2, 3, 4, 5):
#     print("#", i)
