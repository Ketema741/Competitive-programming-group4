# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack, nums = [], []
        
        while head:
            nums.append(head.val)
            head = head.next
            
        res = [0]*len(nums)

        for indx, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                smaller = stack.pop()
                res[smaller] = num
                
            stack.append(indx)
            
        return res