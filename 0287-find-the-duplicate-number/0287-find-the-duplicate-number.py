class Solution:
    def findDuplicate(self, nums):
#         fast = slow = nums[0]
        
#         while True:
#             slow = nums[slow]
#             fast = nums[nums[fast]]
#             if fast == slow:
#                 break
                
#         slow = nums[0]
#         while slow != fast:
#             slow = nums[slow]
#             fast = nums[fast]
        
#         return slow

        res = []
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
                
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return nums[i]
            
