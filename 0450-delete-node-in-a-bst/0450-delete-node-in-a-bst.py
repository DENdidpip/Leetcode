class Solution(object):
    def deleteNode(self, root, key):
        if root is None:
            return None

        parent = None
        node = root

        while node:
            if node.val == key:
                break

            parent = node

            if node.val < key:
                node = node.right
            else:
                node = node.left

        if node is None:
            return root

        if node.left and node.right:
            successor_parent = node
            successor = node.right

            while successor.left:
                successor_parent = successor
                successor = successor.left

            node.val = successor.val

            parent = successor_parent
            node = successor

        if node.left:
            child = node.left
        else:
            child = node.right

        if parent is None:
            return child

        if parent.left == node:
            parent.left = child
        else:
            parent.right = child

        return root
