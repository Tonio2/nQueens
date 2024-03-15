import numpy
import copy


class NQueens:
    def __init__(self, size):
        self.size = size
        self.board = numpy.zeros(shape=(size, size))
        self.moves = []
        self.solutions_count = 0
        self.solutions = []

    def is_out_of_bound(self, row, col):
        if row < 0 or row > self.size - 1:
            return True
        if col < 0 or col > self.size - 1:
            return True
        return False

    def is_legal(self, row, col):
        if 1 in self.board[row, :]:
            return False
        if 1 in self.board[:, col]:
            return False
        if 1 in [
            self.board[row + i, col + i]
            for i in range(-self.size, self.size)
            if not self.is_out_of_bound(row + i, col + i)
        ]:
            return False
        if 1 in [
            self.board[row + i, col - i]  # i = -1 row + i = 1; col - i = 1
            for i in range(-self.size, self.size)
            if not self.is_out_of_bound(row + i, col - i)
        ]:
            return False
        return True

    def solve(self):
        if len(self.moves) == self.size:
            self.solutions_count += 1
            self.solutions.append(copy.deepcopy(self.board))
            return None
        for row in range(self.size):
            for col in range(self.size):
                if self.is_legal(row, col):
                    self.board[row, col] = 1
                    self.moves.append((row, col))
                    self.solve()
                    self.board[row, col] = 0


if __name__ == "__main__":
    n_queens = NQueens(4)
    n_queens.solve()

    for sol in n_queens.solutions:
        print(sol)
        print("_" * 80)
