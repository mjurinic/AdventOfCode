import sys

class Position:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    orientation = x = y = 0

    visited = []

    def update(self, move):
        direction = move[0]
        steps = int(move[1:])

        self.orientation += 1 if direction == 'R' else 3
        self.orientation %= 4

        for i in xrange(steps):
            self.x += self.dx[self.orientation]
            self.y += self.dy[self.orientation]

            if (self.x, self.y) in self.visited:
                return True

            self.visited.append((self.x, self.y))

        return False

    def distance(self):
        return abs(self.x) + abs(self.y)

if __name__ == "__main__":
    position = Position()
    moves = sys.stdin.read().split(",")

    for move in moves:
        if position.update(move.strip()):
            break

    print position.distance()
