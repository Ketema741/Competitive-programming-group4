test_len = int(input())

for _ in range(test_len):
    n = int(input())
    nums = list(map(int, input().split()))
    if n == 1:
        print("YES")
    elif n == 2:
        print("YES" if abs(nums[0] - nums[1]) <= 1 else "NO")
    else:
        nums.sort()
        for i in range(1, n-1):
            if nums[i] - nums[i-1] > 1:
                print("NO")
                break
            else:
                print("YES")

    """  
        1   2   3   4 
        
        5   6   7   8
        
        5   6   7   8
    """ 