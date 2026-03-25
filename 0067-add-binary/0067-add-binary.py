class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        leftover = 0

        while a and b:
            if a[-1] == '0' and b[-1] == '0':
                if not leftover:
                    res += '0'
                else:
                    res += '1'
                    leftover = 0

            elif a[-1] == '1' and b[-1] == '1':
                res += '1' if leftover else '0'
                leftover = 1

            else:  # 0+1 или 1+0
                if leftover:
                    res += '0'
                    leftover = 1
                else:
                    res += '1'

            a = a[:-1]
            b = b[:-1]

        last = a or b

        while last:
            if last[-1] == '0' and leftover:
                res += '1'
                leftover = 0
            elif last[-1] == '1' and leftover:
                res += '0'
                leftover = 1
            else:
                res += last[-1]

            last = last[:-1]

        if leftover:
            res += '1'

        return res[::-1]