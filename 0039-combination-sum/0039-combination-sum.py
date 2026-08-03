class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def tmp(start, currant, total):
            if total == target:
                res.append(currant[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                currant.append(candidates[i])

                tmp(i, currant, total + candidates[i])

                currant.pop()

        tmp(0, [], 0)

        return res