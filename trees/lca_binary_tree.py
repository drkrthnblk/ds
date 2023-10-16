https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        # if either p or q is root then that is lca
        if root.val == p.val or root.val == q.val:
            return root
        # start dfs
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # if we have both child return parent node as it will be the lca
        if left and right:
            return root
        # else return which ever child exists as both p and q will be on 
        # the esisting child side, since we would have covered other child
        # and it would have returned None(not found)
        else:
            return left or right