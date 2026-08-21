class Solution(object):
    def reverseVowels(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u']
        used = []

        s = list(s)

        for i in range(len(s)):
            if s[i].lower() in vowels:
                used.append(s[i])
                s[i] = '_'

        used.reverse()

        for i in range(len(s)):
            if s[i] == '_':
                s[i] = used[0]
                used.pop(0)

        return ''.join(s)