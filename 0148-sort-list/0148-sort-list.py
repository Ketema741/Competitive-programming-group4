# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(list1, list2):
            dummy = head = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    head.next = list1
                    list1 = list1.next
                    head = head.next
                else: 
                    head.next = list2
                    list2 = list2.next
                    head = head.next
                 
            if list2:
                head.next = list2
            if list1:
                head.next = list1
                
            return dummy.next
        
        def backtrack(left):
            
            if not left or not left.next:
                return left
            
            pre, slow, fast = None, left, left
            while fast and fast.next:
                pre, slow, fast = slow, slow.next, fast.next.next
            pre.next = None
                
            left = backtrack(left)
            right = backtrack(slow)
            return merge(left, right)
            
        return backtrack(head)
            
        