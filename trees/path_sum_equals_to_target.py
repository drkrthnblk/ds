https://leetcode.com/problems/path-sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def check(root, curr_sum):

            if not root:
                return False
            
            curr_sum += root.val
            
            # if we reach leaf check if the target is found
            if not root.left and not root.right:
                return curr_sum == targetSum
            
            return check(root.left, curr_sum) or check(root.right, curr_sum)

        return check(root,0)