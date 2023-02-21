# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        
        while head :
            arr.append(head.val)
            head = head.next
            
        left, right = 0, len(arr) - 1
        res = 0
        
        while left < right:
            res = max(res, arr[left] + arr[right])
            left += 1
            right -= 1
            
        return res