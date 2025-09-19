from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        if not root:
            return ans
        
        current = [root]
        while current:
            next_level = []

            for node in current:
                for child in node.children:
                    if child: next_level.append(child)

            ans.append(list(node.val for node in current))
            current = next_level

        return ans



        