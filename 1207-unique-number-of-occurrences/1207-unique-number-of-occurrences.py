class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dictt = {}
        res = []
        for i in range(len(arr)):
            if arr[i] not in dictt:
                dictt[arr[i]] = 1
            else:
                dictt[arr[i]] += 1
        for value in dictt.values():
            res.append(value)
        return len(list(set(res))) == len(res)