# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # call maxDepth recursively
        # store how many layers each search goes through as count
        # only replace the count if a search returns a greater value
        
        if root is None:
            return 0
        
        going_left = self.maxDepth(root.left)
        going_right = self.maxDepth(root.right)
        
        if going_left > going_right:
            return going_left + 1
        else:
            return going_right + 1
