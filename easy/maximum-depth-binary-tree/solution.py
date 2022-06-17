# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        p = root
        
        if p == None:
            return 0
        
        depth_left = self.maxDepth(p.left)
        depth_right = self.maxDepth(p.right)
        
        if depth_left > depth_right:
            return depth_left + 1
        
        else:
            return depth_right + 1
        
        
