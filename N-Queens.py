class Solution:
    def solveNQueens(self, n):
        def backtrack(row, diagonals, antiDiagonals, cols, board):
            if row == n:
                result.append(["".join(r) for r in board])
                return
            for col in range(n):
                currDiagonal = row - col
                currAntiDiagonal = row + col
                if col in cols or currDiagonal in diagonals or currAntiDiagonal in antiDiagonals:
                    continue
                cols.add(col)
                diagonals.add(currDiagonal)
                antiDiagonals.add(currAntiDiagonal)
                board[row][col] = 'Q'
                backtrack(row + 1, diagonals, antiDiagonals, cols, board)
                cols.remove(col)
                diagonals.remove(currDiagonal)
                antiDiagonals.remove(currAntiDiagonal)
                board[row][col] = '.'
        result = []
        board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), board)
        return result
