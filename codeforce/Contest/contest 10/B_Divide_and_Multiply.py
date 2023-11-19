test_len = int(input())

for _ in range(test_len):

    n = int(input())
    nums = list(map(int,input().split()))
    
    res = 0

    for i in range(len(nums)):

        for j in range(len(nums)):
            if i == j or nums[j] %2 != 0:
                continue
            else:
                while nums[j] %2 == 0:
                    nums[i] *= 2
                    nums[j] //= 2
        res = max(res, sum(nums))
    print(res)