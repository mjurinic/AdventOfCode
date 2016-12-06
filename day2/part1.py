import sys

class Position:
    grid = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]

    x = y = 1

    def update(self, move):
        if move == 'U':
            if self.checkMove(self.x - 1, self.y):
                self.x -= 1

        elif move == 'D':
            if self.checkMove(self.x + 1, self.y):
                self.x += 1

        elif move == 'L':
            if self.checkMove(self.x, self.y - 1):
                self.y -= 1

        elif move == 'R':
            if self.checkMove(self.x, self.y + 1):
                self.y += 1

    def checkMove(self, x, y):
        return x >= 0 and x < 3 and y >= 0 and y < 3

if __name__ == "__main__":
    position = Position()

    moves = sys.stdin.read().split("\n")
    del moves[-1]

    sol = ""

    for move in moves:
        for i in move:
            position.update(i)

        sol += position.grid[position.x][position.y]

    print sol
