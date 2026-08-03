class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = "1"
        for i in range(n - 1):
            count, new_res = 1, ""
            for j in range(1, len(res)):
                if res[j] == res[j-1]:
                    count += 1
                else:
                    new_res += str(count)+ res[j-1]
                    count = 1
            new_res += str(count)+ res[-1]
            res = new_res

        return res