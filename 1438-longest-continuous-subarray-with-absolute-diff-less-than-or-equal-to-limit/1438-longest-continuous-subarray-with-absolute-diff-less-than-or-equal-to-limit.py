class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dqMin, dqMax = deque(), deque()
        left = ans = 0
        
        for right in range(len(nums)):
            # add min to the queue
            while dqMin and nums[dqMin[-1]] >= nums[right]:
                dqMin.pop()
            dqMin.append(right)
            
            # add max to the queue
            while dqMax and nums[dqMax[-1]] <= nums[right]:
                dqMax.pop()
            dqMax.append(right)
            
            # If max - min is greater than limit, shrink the window
            while nums[dqMax[0]] - nums[dqMin[0]] > limit:
                left += 1
                if dqMin[0] < left: dqMin.popleft()
                if dqMax[0] < left: dqMax.popleft()
            
            ans = max(ans, right - left + 1)
            
        return ans