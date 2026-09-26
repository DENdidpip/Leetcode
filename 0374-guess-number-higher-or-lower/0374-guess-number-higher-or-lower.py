# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right =0, n
        while left <= right:
            middle = (left + right)//2
            a = guess(middle)
            if a == -1:
                right = middle-1
            elif a == 1:
                left = middle+1
            else:
                return middle
