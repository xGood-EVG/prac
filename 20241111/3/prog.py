MIDDLE_DOT = "·"
FULL_BLOCK = '█'

class Maze:
    def __init__(self, n):
        self.n = n
        self.graph = {(i, j): set() for i in range(n) for j in range(n)}

    def __setitem__(self, key, value):
        coord_1 = key[0], key[1].start
        coord_2 = key[1].stop, key[2]

        for i in range(min(coord_1[0], coord_2[0]), max(coord_1[0], coord_2[0])):
            if value == MIDDLE_DOT:
                self.graph[(i, coord_1[1])].add((i + 1, coord_2[1]))
                self.graph[(i + 1, coord_2[1])].add((i, coord_2[1]))
            else:
                self.graph[(i, coord_1[1])].remove((i + 1, coord_2[1]))
                self.graph[(i + 1, coord_2[1])].remove((i, coord_1[1]))

        for i in range(min(coord_1[1], coord_2[1]), max(coord_1[1], coord_2[1])):
            if value == MIDDLE_DOT:
                self.graph[(coord_1[0], i)].add((coord_2[0], i + 1))
                self.graph[(coord_2[0], i + 1)].add((coord_1[0], i))
            else:
                self.graph[(coord_1[0], i)].remove((coord_2[0], i + 1))
                self.graph[(coord_2[0], i + 1)].remove((coord_1[0], i))

    def __getitem__(self, key):
        coord_1 = key[0], key[1].start
        coord_2 = key[1].stop, key[2]

        visited = set()
        plan_to_visit = [coord_1]
        visited.add(coord_1)

        while plan_to_visit:
            coord = plan_to_visit.pop(0)
            if coord == coord_2:
                return True

            for neighbor in self.graph[coord]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    plan_to_visit.append(neighbor)

        return False

    def __str__(self):
        result = ""
        result += FULL_BLOCK * (self.n * 2 + 1) + '\n'
        for i in range(self.n):
            result += FULL_BLOCK
            for j in range(self.n):
                result += MIDDLE_DOT
                result += MIDDLE_DOT if (j + 1, i) in self.graph[(j, i)] else FULL_BLOCK
            result += '\n'
            result += FULL_BLOCK
            for j in range(self.n):
                result += MIDDLE_DOT if (j, i + 1) in self.graph[(j, i)] else FULL_BLOCK
                result += FULL_BLOCK
            result += '\n'
        return result[:-1]

import sys
exec(sys.stdin.read())