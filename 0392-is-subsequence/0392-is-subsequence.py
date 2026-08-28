class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "" or (s == "" and t == ""):
            return True
        if t == "":
            return False
        s_pointer = 0
        for i in range(len(t)):
            if t[i] == s[s_pointer]:
                s_pointer += 1
            if s_pointer == len(s):
                return True
        return False
        