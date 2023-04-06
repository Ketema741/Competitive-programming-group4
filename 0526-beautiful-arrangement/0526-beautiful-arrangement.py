class Solution:
    def countArrangement(self, N: int) -> int:
        self.count = 0
        nums = [i for i in range(1, N+1)]
        self.permute(nums, 0)
        return self.count
    
    def permute(self, nums: List[int], l: int) -> None:
        if l == len(nums):
            self.count += 1
            return
        
        for i in range(l, len(nums)):
            nums[l], nums[i] = nums[i], nums[l]
            
            if nums[l] % (l+1) == 0 or (l+1) % nums[l] == 0:
                self.permute(nums, l+1)
                
            nums[l], nums[i] = nums[i], nums[l]