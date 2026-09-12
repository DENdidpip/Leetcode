# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        prefix = {0:1}
        def move(node, current_sum):
            if node is None:
                return 0
            current_sum += node.val
            count = prefix.get(current_sum - targetSum, 0)

            prefix[current_sum] = prefix.get(current_sum, 0) + 1
            count += move(node.left, current_sum)
            count += move(node.right, current_sum)

            prefix[current_sum] -= 1

            return count

        return move(root, 0)