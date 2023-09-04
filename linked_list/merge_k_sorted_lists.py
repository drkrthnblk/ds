https://leetcode.com/problems/merge-k-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# solution 1
# merge two lists at a time using merge sorted lists logic

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        res = lists[0]
        for i in range(1, len(lists)):
            res = self.mergeTwoLists(res,lists[i])
        return res

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy=ListNode(0)
        lst1=dummy
        while l1 and l2:
            if l1.val<=l2.val:
                lst1.next=l1
                l1=l1.next
            else:
                lst1.next=l2
                l2=l2.next
            lst1=lst1.next
            
        lst1.next=l1 or l2    
        return dummy.next
		
# solution 2: divide and conquer solution
# merge two lists at a time until we have final list
# so after first pass there will be n/2 nodes and then n/4 and so on

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        last = len(lists) - 1
 
        # repeat until only one list is left
        while last:
            i = 0
            j = last
    
            # `(i, j)` forms a pair
            while i < j:
                # merge list `j` with `i`
                lists[i] = self.mergeTwoLists(lists[i], lists[j])
    
                # consider the next pair
                i = i + 1
                j = j - 1
    
            last = j   
        return lists[0]

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy=ListNode(0)
        lst1=dummy
        while l1 and l2:
            if l1.val<=l2.val:
                lst1.next=l1
                l1=l1.next
            else:
                lst1.next=l2
                l2=l2.next
            lst1=lst1.next
            
        lst1.next=l1 or l2    
        return dummy.next
		
# solution 3