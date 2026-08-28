class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, res = 0, (len(height)-1), 0
        for i in range(len(height)):
            res = max(min(height[left], height[right])*(right - left), res) 
            if height[left] < height[right] or height[left] == height[right]:
                left += 1
            elif height[left] > height[right]:
                right -=1
        return res