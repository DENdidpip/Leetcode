import numpy as np

class Solution(object):
    def findKthLargest(self, nums, k):
        nums = np.array(nums)

        index = len(nums) - k

        return np.partition(nums, index)[index]