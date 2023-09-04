https://leetcode.com/problems/copy-list-with-random-pointer/description/

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        # add dup node
        curr = head
        while curr:
            copy = Node(curr.val, curr.next)
            next = curr.next
            curr.next = copy
            curr = next
            
        # set the random pointer in the copied node from original node
        curr = head
        while curr and curr.next:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
            
        
        # separate the copied list from original list
        # separating the copied list will automaticaly result in
        # 2 lists
        copy = head.next
        curr = copy
        while curr and curr.next:
            curr.next = curr.next.next
            curr = curr.next
        
        return copy