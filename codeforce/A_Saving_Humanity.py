
tes_len = int(input())

for _ in range(tes_len):

    n, m = list(map(int, input().split()))

    nums = [num for num in input()]
    res = []

    if nums[1] == '1' and nums[0] == '0':
            res.append(0) 
    while m:
        left = 0
        
        for right in range(n):
            if right - left < 2:
                continue

            if nums[right - 1] == '0' and nums[right] != nums[left]:
                res.append(right - 1)
           
            left += 1
        
        m -= 1
        while len(res):
            nums[res.pop()] = '1'
        
    print(''.join(nums))
