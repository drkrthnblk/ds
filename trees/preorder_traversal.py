https://leetcode.com/problems/binary-tree-preorder-traversal/

# iterative solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """node > left > right"""
        if not root:
            return []
        stack = list()
        stack.append(root)
        res = list()
        while stack:
            node = stack.pop()
            res.append(node.val)
            # we add right first as it will be picked up last
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res


# recursive solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return res







