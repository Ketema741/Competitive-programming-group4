# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        dummy = behind = ahead = head
        N = 0
        
        while dummy:
            dummy = dummy.next
            N += 1
            
        k = N - k % N
        
        if not k: return head
        
        while ahead.next:
            ahead = ahead.next
            if k > 1:  
                behind = behind.next
            
            k -= 1
            
        ahead.next = head
        head = behind.next
        behind.next = None
        return head