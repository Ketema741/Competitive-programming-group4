test_len = int(input())

for indx in range(test_len):
    n = int(input())
    nums = list(map(int, input().split()))

    left, right = 0, 0

    curr_max = nums[left]
    res = 0

    while right < n:
        if nums[left] * nums[right] > 0:
            curr_max = max(curr_max, nums[right])
            right += 1
        else:
            res += curr_max
            left = right
            curr_max = nums[left]

    res += curr_max

    print(res)