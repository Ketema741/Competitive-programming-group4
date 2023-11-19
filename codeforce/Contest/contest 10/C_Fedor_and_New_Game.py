n, m, k = list(map(int, input().split()))
nums = []

for _ in range(m+1):
    nums.append(int(input()))

fedor = nums[-1]
res = 0
for i in range(m):
    bit_diff = (fedor ^ nums[i])
    
    diff = 0
    while bit_diff:
        if bit_diff&1:
            diff += 1

        bit_diff = bit_diff >> 1

    if diff <= k:
        res += 1
print(res)

