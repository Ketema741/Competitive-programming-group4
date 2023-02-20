# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        fast = head
        count = 0
        while curr:
            curr = curr.next
            count += 1
        middle = math.floor(count / 2)
        
        while middle:
            fast = fast.next
            middle -= 1
        
        
        return fast