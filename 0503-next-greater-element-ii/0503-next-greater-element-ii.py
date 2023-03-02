class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [-1] * N
        stack = []
        
        for i in range(2*N - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i % len(nums)]:
                stack.pop()
            
            if stack:
                res[i % N] = nums[stack[-1]]
            
            stack.append(i % N)
        return res
