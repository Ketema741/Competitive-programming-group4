# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left == right:
            return head
        
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        
        # move pre to the node before the left-th node
        for _ in range(left - 1):
            pre = pre.next
        
        # reverse the nodes between left and right
        cur = pre.next
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
        
        return dummy.next
