# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def move(node, max_value):
            if not node:
                return 0
            if node.val >= max_value:
                self.res += 1
                max_value = node.val
            move(node.left, max_value)
            move(node.right, max_value)
        move(root, root.val)
        return self.res   

        