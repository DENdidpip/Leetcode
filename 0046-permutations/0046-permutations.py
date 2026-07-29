class Solution(object):
    def permute(self, nums):
        from itertools import permutations
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(permutations(nums))
        