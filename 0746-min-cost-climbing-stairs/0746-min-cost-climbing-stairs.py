class Solution(object):
    def minCostClimbingStairs(self, cost):
        memo = {}

        def move(index):
            if index >= len(cost):
                return 0

            if index in memo:
                return memo[index]

            memo[index] = cost[index] + min(
                move(index + 1),
                move(index + 2)
            )

            return memo[index]

        return min(move(0), move(1))