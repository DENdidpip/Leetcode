class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n, m = len(num1), len(num2)
        res = [0] * (n + m)
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])

                p1 = i + j
                p2 = i + j + 1

                total = mul + res[p2]

                res[p2] = total % 10
                res[p1] += total // 10

        result = "".join(map(str, res)).lstrip("0")
        return result if result else "0"
        