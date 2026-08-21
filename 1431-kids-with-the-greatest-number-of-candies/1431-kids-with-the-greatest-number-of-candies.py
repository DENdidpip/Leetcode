class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxim = max(candies)
        res = []
        for i in range(len(candies)):
            res.append((candies[i] + extraCandies) >= maxim)
        return res