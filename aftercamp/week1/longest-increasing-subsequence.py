class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and memo[i] < memo[j] + 1:
                    memo[i] = memo[j] + 1

        return max(memo)