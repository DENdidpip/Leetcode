class Solution(object):
    def minFlips(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        flips = 0
        while(a or b or c):
            bit_a, bit_b, bit_c =a&1, b&1, c&1
            if not bit_c:
                flips += bit_a + bit_b
            elif not bit_a and not bit_b:
                flips += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return flips