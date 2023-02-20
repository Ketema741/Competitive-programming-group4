# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        cycle = False
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                cycle = True
                break
        
        while cycle and head != fast:
            head = head.next
            fast = fast.next
        
        return head if cycle else None