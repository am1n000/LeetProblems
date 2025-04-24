# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def checkBiggest(node, biggest):
            if not node:
                return 0
            res = 0
            if node.val >= biggest:
                res = 1
            if node.val > biggest:
                biggest = node.val
            res += checkBiggest(node.left, biggest)
            res += checkBiggest(node.right, biggest)
            return res
        
        return checkBiggest(root, root.val)