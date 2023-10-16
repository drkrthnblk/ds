https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None
import collections

class Solution:
    def bottomView(self, root):
        if not root:
            return
        
        hd = 0
        
        m = dict()
        mh = dict()
     
        q = []
        mh[root] = hd
        q.append(root)  
     
        while q:
            temp = q.pop(0)
            
            hd = mh[temp]
     
            # if horizontal dist already encountered
            # replace with new value as it will at bottom
            m[hd] = temp.data
     
            if temp.left:
                mh[temp.left] = hd - 1
                q.append(temp.left)
     
            if temp.right:
                mh[temp.right] = hd + 1
                q.append(temp.right)

        ans = [m[i] for i in sorted(m.keys())]
        return ans

