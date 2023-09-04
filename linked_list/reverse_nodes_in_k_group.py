https://leetcode.com/problems/reverse-nodes-in-k-group/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head; count = 0
        prev = None; next = None
        
        # if the given list is not reversible, contains less nodes
        # just return it
        total_count = 0
        while curr != None:
            total_count += 1
            curr = curr.next
            
        curr = head
        if total_count < k:
            return curr
        
        # reverse in goup of K or till node exists
        while count < k and curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr= next
            count += 1
            
        # if we have next set of nodes, process those
        if next != None:
                head.next = self.reverseKGroup(next, k)
        return prev