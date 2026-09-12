class Solution(object):
    def longestZigZag(self, root):
        
        def dfs(node, left, right):
            if node is None:
                return 0

            a = dfs(node.left, right + 1, 0)
            b = dfs(node.right, 0, left + 1)

            return max(left, right, a, b)

        return dfs(root, 0, 0)