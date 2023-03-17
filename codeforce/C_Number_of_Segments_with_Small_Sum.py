n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
res =sum_ = 0

left = 0
for right in range(n):
    sum_ += nums[right]
    
    while sum_ > k:
        sum_ -= nums[left]
        left += 1
    res +=  right - left + 1
    
print(res)