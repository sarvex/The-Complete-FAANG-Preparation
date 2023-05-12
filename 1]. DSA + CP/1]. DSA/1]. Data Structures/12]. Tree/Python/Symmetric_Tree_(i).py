# Symmetric Tree - Recursion
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def compareSubtrees(self, root1, root2):

        if root1 is None and root2 is None:
            return True
        elif root1 is None or root2 is None or (root1.val != root2.val):
            return False
        else:
            return self.compareSubtrees(root1.left, root2.right) and self.compareSubtrees(root1.right, root2.left)

    def isSymmetric(self, root) -> bool:

        if root.left is None and root.right is None:
            return True

        return self.compareSubtrees(root.left, root.right)

# Time Complexity: O(N)
# Space Complexity: O(N)
