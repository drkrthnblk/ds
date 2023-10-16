https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    max_level = [0]
    res = list()
    leftViewUtil(root, 1, max_level, res)
    return res
    
def leftViewUtil(root, level, max_level, res):
    if not root:
        return
    
    if level > max_level[0]:
        res.append(root.data)
        max_level[0] = level
        
    leftViewUtil(root.left, level + 1, max_level, res)
    leftViewUtil(root.right, level + 1, max_level, res)

