https://practice.geeksforgeeks.org/problems/diagonal-traversal-of-binary-tree/1


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Complete the function below
class Solution:
    def diagonal(self,root):
        #:param root: root of the given tree.
        #return: print out the diagonal traversal,  no need to print new line
        diag_sum = dict()
        self.diagSum(root, 0, diag_sum)
        return [ele for lists in diag_sum.values() for ele in lists ]

    def diagSum(self, root, level, diag_sum):
        if root:
            if level not in diag_sum:
                diag_sum[level] = [root.data]
            else:
                diag_sum[level].append(root.data)
                
            self.diagSum(root.left, level + 1, diag_sum)
            self.diagSum(root.right, level, diag_sum)


