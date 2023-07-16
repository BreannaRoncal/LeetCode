"""
Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
  Input: root = [1,2,2,3,4,4,3]
  Output: true
  
Example 2:
  Input: root = [1,2,2,null,3,null,3]
  Output: false
 

Constraints:
  - The number of nodes in the tree is in the range [1, 1000].
  - 100 <= Node.val <= 100


Solution using recursion
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self, left, right):
        # Base case: it reaches the end of the tree return True
        if not left and not right:
            return True
        # If one side reaches None first, then it is not symmetrical
        elif not left or not right:
            return False
        # If the left and right tree values equals each other, then recursively check the next two sides
        else:
            return left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
