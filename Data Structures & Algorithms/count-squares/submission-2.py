class CountSquares:
    '''
    Time: O(1) for add, O(n) for count

    Space: O(n) for list and dict
    '''
    def __init__(self):
        self.pointsCount = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.pointsCount[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        px, py = point
        res = 0

        # find all diagonals possible for the point and then find squares
        for x, y in self.points:
            # if diagonal point of square exists
            # we can find other 2 points in O(1) time
            if abs(px - x) != abs(py - y) or x == px or y == py:
                continue

            # if px, py and x, y are diagonals of a square
            # other two points are px, y and x, py
            # since we can have duplicates, multiply and return count of squares
            res += self.pointsCount[(px, y)] * self.pointsCount[(x, py)]

        return res
