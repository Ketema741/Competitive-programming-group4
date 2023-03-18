n, k = list(map(int, input().split()))
nums = sorted(list(map(int, input().split())))

res = count = 0
if k == 0:
    res = nums[0] - 1
else:
    res = nums[k-1]

for i in range(n):
    if nums[i] <= res:
        count += 1
# if count > k or res not in range [1, 10**9]
if k != count or not (1 <= res <= 10**9):
    print("-1")
else:
    print(res)