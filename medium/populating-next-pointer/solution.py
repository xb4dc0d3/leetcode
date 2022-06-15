"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        def traverse_helper(root1, root2):
            if not root1:
                return
            
            if not root2:
                return
            
            root1.next = root2
            traverse_helper(root1.left, root1.right)
            traverse_helper(root2.left, root2.right)
            traverse_helper(root1.right, root2.left)
            
            return 
            
            
        if not root:
            return
        
        traverse_helper(root.left, root.right)
        
        return root
            
            
            
        
