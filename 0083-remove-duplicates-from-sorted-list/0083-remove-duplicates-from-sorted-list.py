# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = head
        
        while front and front.next:
            if front.val == front.next.val:
                front.next = front.next.next
            else:
                front = front.next
                
        return head
        