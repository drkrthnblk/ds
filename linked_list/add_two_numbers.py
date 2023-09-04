https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_head = l1
        l2_head = l2
        carry = 0
        temp = ListNode(0)
        curr = temp
        while l1_head and l2_head:
            sum = l1_head.val + l2_head.val + carry
            curr.next = ListNode(sum%10)
            carry = sum//10
            
            l1_head = l1_head.next
            l2_head = l2_head.next
            curr = curr.next
            
        while l1_head:
            sum = l1_head.val + carry
            curr.next = ListNode(sum%10)
            carry = sum//10
            l1_head = l1_head.next
            curr = curr.next
            
        while l2_head:
            sum = l2_head.val + carry
            curr.next = ListNode(sum%10)
            carry = sum//10
            l2_head = l2_head.next
            curr = curr.next
        
        if carry:
            curr.next = ListNode(carry)
        
        return temp.next
