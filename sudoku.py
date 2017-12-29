import argparse


class Sudoku:
    def __init__(self, s):
        self.grid = [int(i) for i in s]

    def __str__(self):
        s = ''
        i = 0
        for c in self.grid:
            i = i + 1
            s = s + str(c) + ' '

            if i % 3 == 0 and i % 9 != 0:
                s = s + "| "
            if i % 9 == 0:
                s = s + "\n"
            if i % 27 == 0 and i % 81 != 0:
                s = s + '------+-------+------\n'

        return s

    @classmethod
    def from_file(cls, filename):
        with open(filename) as file:
            line = file.read().replace(' ', '').replace('\n', '')
            return Sudoku(line)

    def to_line(self):
        s = ''
        for i in self.grid:
            s = s + str(i)
        return s

    def row(self, i):
        c = []
        for j in range(9):
            c.append(self.grid[i * 9 + j])
        return c

    def column(self, i):
        c = []
        for j in range(9):
            c.append(self.grid[j * 9 + i])
        return c

    def block(self, i):
        c = []
        b = 9 * (i - i % 3) + (i % 3 * 3)
        for j in range(3):
            for k in range(3):
                c.append(self.grid[j * 9 + k + b])
        return c

    def row_idx(self, i):
        return i // 9

    def column_idx(self, i):
        return i % 9

    def block_idx(self, i):
        return self.row_idx(i) // 3 * 3 + self.column_idx(i) // 3

    def is_valid(self):
        if len(self.grid) != 81:
            return False
        if 0 in self.grid:
            return False

        for i in range(9):
            if len(set(self.row(i))) != 9 or len(set(
                    self.column(i))) != 9 or len(set(self.block(i))) != 9:
                return False

        return True

    def solve(self):
        if 0 not in self.grid:
            return True

        i = self.grid.index(0)

        for c in range(1, 10):
            if c not in self.row(self.row_idx(i)) and c not in self.column(
                    self.column_idx(i)) and c not in self.block(
                        self.block_idx(i)):
                self.grid[i] = c
                if self.solve():
                    return True

        self.grid[i] = 0
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Solve Sudoku Puzzle with backtracking algorithm')
    parser.add_argument('file_name', help='text file containing Sudoku Puzzle')
    args = parser.parse_args()

    s = Sudoku.from_file(args.file_name)

    print(s)
    s.solve()
    print(s)

    print(s.is_valid())