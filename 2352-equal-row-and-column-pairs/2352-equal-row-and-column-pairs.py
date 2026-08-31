class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        rows = {}
        for row in grid:
            row = tuple(row)

            if row not in rows:
                rows[row] = 1
            else:
                rows[row] += 1

        for i in range(len(grid[0])):
            tmp = []
            for column in grid:
                tmp.append(column[i])
            tmp = tuple(tmp)
            if tmp in rows:
                res += rows[tmp]
        return res