https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        fptr = sptr = dummy

        # move fast ptr to n positions
        for _ in range(n):
            fptr = fptr.next
        
        # move both ptr at same time
        # once fptr reaches end sptr will be one before the delete node
        while fptr and fptr.next :
            fptr=fptr.next
            sptr=sptr.next
        
        # delete node
        sptr.next=sptr.next.next
        return dummy.next
