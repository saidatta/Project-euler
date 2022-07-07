import requests
import timeit

class Solution:
    def solveSudoku(self, board: 'List[List[str]]') -> 'None':
        self.board = board
        self.solve()

    def findUnassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == '0':
                    return row, col
        return -1, -1

    def solve(self):
        row, col = self.findUnassigned()
        if (row, col) == (-1, -1):
            return True

        for num in map(str, range(1, 10)):
            if self.isSafe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = '0'

    def isSafe(self, row, col, ch):
        rowSafe = all(self.board[row][_] != ch for _ in range(9))
        colSafe = all(self.board[_][col] != ch for _ in range(9))
        squareSafe = all(self.board[r][c] != ch for r in self.getRange(row) for c in self.getRange(col))
        return rowSafe and colSafe and squareSafe

    def getRange(self, x):
        x -= x % 3
        return range(x, x + 3)


r = requests.get('https://projecteuler.net/project/resources/p096_sudoku.txt')
grid_num = 0
sudoku_board = []
ans = 0
start = timeit.default_timer()
s = Solution()

for line in r.iter_lines():
    line = line.decode('utf-8')
    if("Grid 50" in line):
        print("final")
    if not 'Grid' in line:
        sudoku_board.append(list(line))
    else:
        if grid_num >= 1:
            s.solveSudoku(board=sudoku_board)
            ans += int("".join(str(x) for x in sudoku_board[0][0:3]))
            print("%s - %d - %d" % (line, grid_num , ans))

            sudoku_board = []
        grid_num += 1

s.solveSudoku(board=sudoku_board)
print("%s - %d - %d" % ("final", grid_num , ans))


stop = timeit.default_timer()
print('Time: ', stop - start)
