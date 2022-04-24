https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.check_mirror(root.left, root.right)
    
    def check_mirror(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        return node1.val == node2.val and self.check_mirror(node1.left, node2.right) \
        and self.check_mirror(node1.right,node2.left)
    