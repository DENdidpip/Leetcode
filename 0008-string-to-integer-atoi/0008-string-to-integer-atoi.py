class Solution(object):
    def myAtoi(self, s):
        res, minus = 0, 1

        INT_MAX, INT_MIN = 2147483647, -2147483648

        while len(s) > 0 and s[0] == " ":
            s = s[1:]

        if len(s) == 0:
            return 0

        if s[0] == "-":
            minus = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        while len(s) > 0 and s[0].isdigit():
            digit = int(s[0])

            if minus == 1:
                if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
                    return INT_MAX
            else:
                if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 8):
                    return INT_MIN

            res = res * 10 + digit
            s = s[1:]

        return res * minus