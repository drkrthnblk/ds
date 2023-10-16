https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1


# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None
import collections
class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        dist_map = dict()
        self.topViewUtil(root, 0, 0, dist_map)
        
        res = [str(dist_map.get(ele)[0]) for ele in sorted(dist_map.keys())]
        return res
        
    def topViewUtil(self, root, dist, level, dist_map):
        if not root:
            return
        
        # Check whether the current horizontal distance is already visited or not?
        # If visited then is previous visited element has greater level.
        if dist not in dist_map.keys() or dist_map[dist][1] > level:
            dist_map[dist] = (root.data, level)

        self.topViewUtil(root.left, dist - 1, level + 1, dist_map)
        self.topViewUtil(root.right, dist + 1, level + 1, dist_map)

# soluion 2: deque

class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
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
            if not hd in m:
                m[hd] = temp.data
     
            if temp.left:
                mh[temp.left] = hd - 1
                q.append(temp.left)
     
            if temp.right:
                mh[temp.right] = hd + 1
                q.append(temp.right)

        ans = [m[i] for i in sorted(m.keys())]
        return ans
