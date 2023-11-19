n, t = map(int, input().split())
nums = list(map(int, input().split()))

right = 0 
tot = 0
res = 0

for i in range(n):
    while right < n and tot + nums[right] <= t:
        tot += nums[right]
        right += 1
    res = max(res, right - i)  
    tot -= nums[i] 
print(res)
