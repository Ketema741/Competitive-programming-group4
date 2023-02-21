# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum_ = num1 = num2 = 0
        indx = 0
        dummy = head = ListNode()
        while l1:
            num1 += l1.val*10**indx
            indx += 1
            l1 = l1.next
        indx = 0
        
        while l2:
            num2 += l2.val*10**indx
            indx += 1
            l2 = l2.next
        sum_ = num1 + num2
        if not sum_: return head
        while sum_:
            val = sum_ % 10
            sum_ = sum_ // 10
            newNode = ListNode(val)
            dummy. next = newNode
            dummy = dummy.next
        return head.next
            