class Solution(object):
    def equalPairs(self,grid):
        n = len(grid)
        row_count = Counter(tuple(row) for row in grid)
        result = 0
        for col in range(n):
            column_tuple = tuple(grid[row][col] for row in range(n))
            result += row_count[column_tuple]

        return result
