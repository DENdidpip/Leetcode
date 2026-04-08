class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def dfs(curr, used_open, used_close):
            if len(curr) == 2 * n:
                res.append(curr)
                return

            if used_open < n:
                dfs(curr + "(", used_open + 1, used_close)

            if used_close < used_open:
                dfs(curr + ")", used_open, used_close + 1)

        dfs("", 0, 0)
        return res
