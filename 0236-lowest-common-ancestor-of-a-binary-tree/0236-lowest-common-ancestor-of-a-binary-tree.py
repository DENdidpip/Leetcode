class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        def dfs(node):
            if node is None:
                return None

            if node == p or node == q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node

            if left:
                return left

            return right

        return dfs(root)