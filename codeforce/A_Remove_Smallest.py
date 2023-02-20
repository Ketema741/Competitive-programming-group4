test_len = int(input())

for _ in range(test_len):
    n = int(input())
    nums = sorted(list(map(int, input().split())))
    if n == 1:
        print("YES")
    elif n == 2:
        print("YES" if abs(nums[0] - nums[1]) <= 1 else "NO")
    else:
        valid = True
        for right in range(1, n):
            if abs(nums[right] - nums[right - 1]) > 1:
                valid = False
                break
        if valid:  
            print("YES")
        else:
            print("NO")