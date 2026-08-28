class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, (len(height)-1)
        res = 0
        for i in range(len(height)):
            min_wall = min(height[left], height[right])
            amount = min_wall*(right - left)
            if amount > res:
                res = amount
            if height[left] < height[right] or height[left] == height[right]:
                left += 1
            elif height[left] > height[right]:
                right -=1
        return res