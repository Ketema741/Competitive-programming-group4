class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queuee = deque()
        res = []
        left = right = 0
        
        while right < len(nums):
            while queuee and nums[queuee[-1]] < nums[right]:
                queuee.pop()
            queuee.append(right)
            
            if left > queuee[0]:
                queuee.popleft()
            
            if right + 1 >= k:
                res.append(nums[queuee[0]])
                left += 1
                
            right += 1
            
        return res