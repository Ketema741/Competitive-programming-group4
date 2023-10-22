# Time Complexity - O(nlogn)
# Space Complexity - O(1)

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res, mod = 0, (10**9 + 7)

        right = len(nums) - 1
        for left in range(len(nums)):
            while (nums[left] + nums[right]) > target and left <= right:
                right -= 1

            if left <= right:
                res +=  (1<<(right - left)) # x << n == x*(2**n)
                res %= mod

        return res