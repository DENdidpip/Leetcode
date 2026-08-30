class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = {'a', 'e', 'i', 'o', 'u' }
        window = s[:k]
        curr =0
        for i in window:
            if i in vowels:
                curr+=1
        res = curr
        
        for i in range(len(s) - k):
            if s[i] in vowels:
                curr -= 1

            if s[i + k] in vowels:
                curr += 1

            res = max(res, curr)

        return res

            
        