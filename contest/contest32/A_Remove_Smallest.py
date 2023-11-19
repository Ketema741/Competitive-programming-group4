def canSingleElement(n, nums):
    nums.sort() 
    for i in range(n - 1):
        if nums[i + 1] - nums[i] > 1:
            return "NO" 
    return "YES" 


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    result = canSingleElement(n, nums)
    print(result)
