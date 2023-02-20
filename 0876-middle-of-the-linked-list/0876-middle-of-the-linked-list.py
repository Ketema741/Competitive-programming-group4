# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        dummy = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        middle = count // 2
        
        while middle:
            dummy = dummy.next
            middle -= 1
        
        return dummy