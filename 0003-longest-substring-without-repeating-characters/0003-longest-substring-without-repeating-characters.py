class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp_set = set()
        left, res_len = 0, 0
        for right in range(len(s)):
            while s[right] in tmp_set:
                tmp_set.remove(s[left])
                left += 1
            tmp_set.add(s[right])
            if res_len < right - left + 1:
                res_len = right - left + 1
        return res_len


