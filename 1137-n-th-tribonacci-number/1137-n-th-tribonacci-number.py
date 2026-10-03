class Solution(object):
    def tribonacci(self, n):
        trib = [0, 1, 1]

        if n < 3:
            return trib[n]

        for i in range(3, n + 1):
            trib.append(sum(trib))
            trib = trib[1:]

        return trib[2]