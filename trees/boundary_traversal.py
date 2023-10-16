https://practice.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def printBoundaryView(self, root):
        # Code here
        res = list()
        res.append(root.data)
        self.printLeftSide(root.left, res)
        self.printLeaves(root.left, res)
        self.printLeaves(root.right, res)
        self.printRightSide(root.right, res)
        return res
        
    def printLeftSide(self, root, res):
        if root:
            if root.left:
               res.append(root.data)
               self.printLeftSide(root.left, res)
            elif root.right:
                res.append(root.data)
                self.printLeftSide(root.right, res)
    
    def printLeaves(self, root, res):
        if root:
            if not root.left and not root.right:
                res.append(root.data)
            self.printLeaves(root.left, res)
            self.printLeaves(root.right, res)
        
    def printRightSide(self, root, res):
        if root:
            if root.right:
                self.printRightSide(root.right, res)
                res.append(root.data)
            elif root.left:
                self.printRightSide(root.left, res)
                res.append(root.data)


