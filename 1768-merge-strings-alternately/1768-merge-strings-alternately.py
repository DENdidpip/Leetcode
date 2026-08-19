class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""
        while word1 and word2:
            res += word1[0]
            res += word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
        res += word1
        res += word2
        return res
        