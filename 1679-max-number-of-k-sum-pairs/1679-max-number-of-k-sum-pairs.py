class Solution(object):
    def maxOperations(self, nums, k):
        seen = {}
        result = 0

        for num in nums:
            need = k - num

            if seen.get(need, 0) > 0:
                result += 1
                seen[need] -= 1
            else:
                seen[num] = seen.get(num, 0) + 1

        return result