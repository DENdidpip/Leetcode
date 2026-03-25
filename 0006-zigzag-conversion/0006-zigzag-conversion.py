class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""]*numRows
        cur_row = 0
        down = False

        for i in s:
            rows[cur_row] += i
            if cur_row == 0 or cur_row == numRows - 1:
                down = not down
            cur_row += 1 if down else -1
        return "".join(rows)