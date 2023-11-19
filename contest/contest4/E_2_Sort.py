test_len = int(input())

for _ in range(test_len):
    count = 0
    n, k = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    
    left = 0
    for right in range(1, n):
        if nums[right-1] >= nums[right]*2  :
            left = right
            
        if right - left == k:
            count += 1
            left += 1
    print(count)