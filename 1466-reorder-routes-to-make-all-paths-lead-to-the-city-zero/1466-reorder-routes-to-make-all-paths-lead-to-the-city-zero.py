class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """

        graph = [[] for _ in range(n)]

        for a, b in connections:
            graph[a].append((b, 1))
            graph[b].append((a, 0))

        visited = set()

        def dfs(city):
            visited.add(city)
            result = 0

            for next_city, change in graph[city]:
                if next_city not in visited:
                    result += change
                    result += dfs(next_city)

            return result

        return dfs(0)
            