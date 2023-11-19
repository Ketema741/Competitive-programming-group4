import math


def subArry(nums, k):
    n = len(nums)
    res = 
    for i in range(n - k + 1):
        sum_ = 0
        for j in range(i, i+k):
            sum_ += nums[j]
        res = max(res, sum_)
    print(res)

def slidingWind(nums, k):
    n = len(nums)
    sum_ = left = res = 0

    for right in range(n):
        sum_ += nums[right]
        if right - left > k - 1:
            sum_ -= nums[left]
            left += 1
        res = max(res, sum_)
    print(res)
    
slidingWind([0,1,3,2,1,5], 3)

