class Solution(object):
    def longestOnes(self, nums, k):
        res = 0
        left = 0
        count_of_zeros = 0

        for right in range(len(nums)):

            if nums[right] == 0:
                count_of_zeros += 1

            while count_of_zeros > k:
                if nums[left] == 0:
                    count_of_zeros -= 1
                left += 1

            res = max(res, right - left + 1)

        return res