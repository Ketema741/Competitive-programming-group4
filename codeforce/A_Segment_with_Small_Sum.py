n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
res =sum_ = 0

left = 0
for right in range(n):
    sum_ += nums[right]
    
    while sum_ > k:
        sum_ -= nums[left]
        left += 1
    res = max(res, right - left + 1)
    
print(res)


"""for i in range(n):
    cur_sum = 0
    
    for j in range(i, n):
        cur_sum += nums[j]
        
        if cur_sum <= k:
            res = max(res, j - i + 1)
        else: break
        
print(res)"""