# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def checkValid(root, lower, upper):
            if not root:
                return True
            if root.val > lower and root.val < upper:
                return checkValid(root.left, lower, root.val) and checkValid(root.right, root.val, upper)
            return False
        return checkValid(root, float("-inf"), float("inf"))