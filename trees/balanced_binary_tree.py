https://leetcode.com/problems/balanced-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) >= 0
    
    # use dfs to traverse to leaf and then calculate the height for each node
    def height(self, root):
        if not root:
            return 0
        
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        # exit conditions
        if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
            return -1
        # return height for recursion stack
        return max(left_height, right_height) + 1