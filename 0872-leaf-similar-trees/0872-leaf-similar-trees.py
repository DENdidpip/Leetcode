# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        
        def move_1(node1, mass):
            if node1 is None:
                return
            
            if node1.left is None and node1.right is None:
                mass.append(node1.val)
                return
            move_1(node1.left, mass)
            move_1(node1.right, mass)
        mass1, mass2 = [], []    
        move_1(root1, mass1)
        move_1(root2, mass2)
        return mass1 == mass2