
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left, right = 1, max(piles)
        res = right
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            for i in piles:
                hours += (i + mid - 1) // mid
            if hours > h:
                left = mid+1
            else:
                res = mid
                right = mid-1
        return res
