class Triangle():
    def __init__(self, d1, d2, d3):
        self.d1 = list(d1)
        self.d2 = list(d2)
        self.d3 = list(d3)
        
    def __str__(self):
        return f"{self.d1}{self.d2}{self.d3}"

    def __abs__(self):
        x1, y1 = self.d1
        x2, y2 = self.d2
        x3, y3 = self.d3
        S = abs((x1 * (y2-y3) + x2 * (y3-y1) + x3 * (y1-y2)) / 2.0)
        return S if S != 0.0 else 0

    def __bool__(self):
        return self.__abs__() != 0

    def __lt__(self, other):
        return self.__abs__() < other.__abs__()

    def __point__(self, point):
        x, y = point
        x1, y1 = self.d1
        x2, y2 = self.d2
        x3, y3 = self.d3

        area = abs(self)
        area1 = abs(Triangle((x, y), self.d2, self.d3))
        area2 = abs(Triangle(self.d1, (x, y), self.d3))
        area3 = abs(Triangle(self.d1, self.d2, (x, y)))
        return abs(area - (area1 + area2 + area3)) < 1e-9
    
    def __contains__(self, other):
        if not bool(other):
            return True
        if not bool(self):
            return False
        return (self.__point__(other.d1) and
                self.__point__(other.d2) and
                self.__point__(other.d3)
               )

    def __and__(self, other):
        if not self or not other:
            return False
        return (self.__point__(other.d1) or
                self.__point__(other.d2) or
                self.__point__(other.d3) or
                other.__point__(self.d1) or
                other.__point__(self.d2) or
                other.__point__(self.d3))

import sys
exec(sys.stdin.read())
