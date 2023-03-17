import math


n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
res = 0
sum_ = left = 0


for right in range(n):
    sum_ += nums[right]
    
    while sum_ >= k:
        
        sum_ -= nums[left]
        left += 1
    res +=   left
        
print(res)