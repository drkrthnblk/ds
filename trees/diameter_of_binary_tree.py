https://leetcode.com/problems/diameter-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.getDiameter(root)
        return self.max_diameter
    
    def getDiameter(self, root):
        if not root:
            return 0
        
        left_depth = self.getDiameter(root.left)
        right_depth = self.getDiameter(root.right)
        
        # get the maximum diameter
        # dia = left height + right height
        self.max_diameter = max(self.max_diameter, left_depth + right_depth)
        # return new height to calculate dia for prev level
        return max(left_depth, right_depth) + 1