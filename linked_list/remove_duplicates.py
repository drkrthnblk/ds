https://leetcode.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        curr = head.next
        prev = head
        
        while curr:
            # print(prev.val, curr.val)
            if prev.val == curr.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head