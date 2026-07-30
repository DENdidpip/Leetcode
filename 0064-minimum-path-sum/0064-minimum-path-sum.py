class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid[0]), len(grid)
        path = [[0] * n for i in range(m)]
        path[0][0] = grid[0][0]
        for i in range(1, n):
            path[0][i] = path[0][i-1] + grid[0][i]
        for j in range(1, m):
            path[j][0] = path[j-1][0] + grid[j][0]
        for i in range(1, m):
            for j in range(1, n):
                path[i][j] = min(path[i-1][j], path[i][j-1]) + grid[i][j]
        return path[-1][-1]