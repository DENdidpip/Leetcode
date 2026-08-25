class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split(" ")
        while '' in arr:
            arr.remove('')
        return " ".join(arr[::-1])