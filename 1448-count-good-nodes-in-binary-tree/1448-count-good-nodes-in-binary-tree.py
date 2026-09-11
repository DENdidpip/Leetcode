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
        def move(node, max_value):
            if node is None:
                return 0
            if node.val >= max_value:
                good = 1
            else:
                good =0 
            max_value = max(max_value, node.val)
            return good + move(node.left, max_value) + move(node.right, max_value)

        return move(root, root.val)
            

        