from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid), len(grid[0])
        q = deque()
        flag = False
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                    flag = True

        time = 0

        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx, ny))
            time+=1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        if time == 0:
            return 0
        return time-1


        
        