class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        prefix_sum = [0]*(n +1)

        for start, end in requests:
            prefix_sum[start] += 1
            prefix_sum[end + 1] -= 1

        for i in range(1, n):
            prefix_sum[i] += prefix_sum[i - 1]
        
        prefix_sum = sorted(prefix_sum[:-1])
        nums.sort()
        res = 0

        for i in range(n):
            res += (nums[i] * prefix_sum[i])
        
        return res%MOD
    

"""
    1 2 3 3 3
    0 1 2 3 4 5
    0 0 0 0 0 0
    ^

    0 1  2 3  4
    1 1 -1 0 -1
    1 2  1 1 0
    0 1 1 1 2
    1 2 3 4 5
    2 + 3 + 4 + 10 = 19

    5 4 3 2 1
    ^ ^ 

    5 9 11 13 14
    8 

    

"""