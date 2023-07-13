"""
Maximum Depth of Binary Tree

Example 1:
  Input: root = [3,9,20,null,null,15,7]
  Output: 3
  
Example 2:
  Input: root = [1,null,2]
  Output: 2
 

Constraints:
  - The number of nodes in the tree is in the range [0, 104].
  - 100 <= Node.val <= 100


Recursive Solution
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
