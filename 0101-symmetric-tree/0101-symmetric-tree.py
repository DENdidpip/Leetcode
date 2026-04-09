class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def mir(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False

            if left.val != right.val:
                return False

            return mir(left.left, right.right) and mir(left.right, right.left)
        
        return mir(root, root)
