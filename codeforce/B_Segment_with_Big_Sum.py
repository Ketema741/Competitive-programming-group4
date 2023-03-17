import math


n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
res = math.inf
sum_ = left = 0 


for right in range(n):
    sum_ += nums[right]
    
    while sum_ >= k:
        res =  min(res, right - left + 1)
        sum_ -= nums[left]
        left += 1
        
if res == math.inf:
    print(-1)
else:
    print(res)