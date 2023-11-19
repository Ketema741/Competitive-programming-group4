n = int(input())
nums = sorted(list(map(int, input().split())), reverse=True)


if (nums[1] + nums[2]) > nums[0]:
    nums[0], nums[1] = nums[1], nums[0]
    print("YES")
    print(*nums) 
else:
    print('NO')