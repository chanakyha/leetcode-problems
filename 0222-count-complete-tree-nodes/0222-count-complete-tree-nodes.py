# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
    
        
        def traverse(node, count = 0):
            if not node:
                return count + 1

            
            return traverse(node.left, count) + traverse(node.right, count)
            

        return (traverse(root) - 1)

