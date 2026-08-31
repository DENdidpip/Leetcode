class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        dictt1, dictt2 = {}, {}
        for char in range(len(word1)):
            if word1[char] not in dictt1:
                dictt1[word1[char]] = 1
            else:
                dictt1[word1[char]] += 1
        for char in range(len(word2)):
            if word2[char] not in dictt2:
                dictt2[word2[char]] = 1
            else:
                dictt2[word2[char]] += 1
        return set(dictt2.keys()) == set(dictt1.keys()) and sorted(dictt2.values()) == sorted(dictt1.values())