class Solution(object):
    def totalNQueens(self, n):
        def backtrack(row, cols, diagonals1, diagonals2):
            if row == n:
                return 1
            
            count = 0
            for col in range(n):
                diag1 = row - col
                diag2 = row + col
                if col in cols or diag1 in diagonals1 or diag2 in diagonals2:
                    continue
                
                cols.add(col)
                diagonals1.add(diag1)
                diagonals2.add(diag2)
                
                count += backtrack(row + 1, cols, diagonals1, diagonals2)
                
                cols.remove(col)
                diagonals1.remove(diag1)
                diagonals2.remove(diag2)
            
            return count
        
        return backtrack(0, set(), set(), set())
