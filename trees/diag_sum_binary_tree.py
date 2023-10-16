https://practice.geeksforgeeks.org/problems/diagonal-sum-in-binary-tree/1

'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Complete the function below
def diagonalSum(root):
    #:param root: root of the given tree.
    
    diag_sum = dict()
    diagSum(root, 0, diag_sum)
    return diag_sum.values()
    
def diagSum(root, level, diag_sum):
    if not root:
        return
    if level not in diag_sum:
        diag_sum[level] = root.data
    else:
        diag_sum[level] += root.data
        
    diagSum(root.left, level + 1, diag_sum)
    diagSum(root.right, level, diag_sum)
    