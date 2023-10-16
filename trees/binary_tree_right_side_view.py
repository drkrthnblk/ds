https://leetcode.com/problems/binary-tree-right-side-view/description/

# solution 1: recursion

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        self.PrintRightView(root, 1, [0], res)
        return res

    def PrintRightView(self, root, level, max_level, res):
        if not root:
            return
        
        if level > max_level[0]:
            res.append(root.val)
            max_level[0] = level
            
        self.PrintRightView(root.right, level+1, max_level, res)
        self.PrintRightView(root.left, level+1, max_level, res)
        
# solution 2: dequeue

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            # after the loop ends rightSide will always contain the
            # rightmost node value, so append it to res
            if rightSide:
                res.append(rightSide.val)
        return res