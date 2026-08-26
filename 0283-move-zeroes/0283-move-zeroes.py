class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)-1, -1, -1):
        #     if nums[i] == 0:
        #         nums.
        count = 0
        while 0 in nums:
            count += 1
            nums.remove(0)
        for i in range(count):
            nums.append(0)