class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        results = []

        def findNsum(l, r, target, N, result):
            if r - l + 1 < N or N < 2 :  
                return
                
            if N == 2: 
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r + 1):
                    if i == l or (i > l and nums[i - 1] != nums[i]):
                        findNsum(i + 1, r, target - nums[i], N - 1, result + [nums[i]])

        findNsum(0, len(nums) - 1, target, 4, [])

        return results