class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ar = s.split()
        if not ar:
            return 0
        return len(ar[-1])