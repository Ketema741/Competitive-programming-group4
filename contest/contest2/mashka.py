N  = list(map(int, input().split()))
theorems = [int(x) for x in input().split()]
sleep_awake = [int(x) for x in input().split()]

n, k = int(N[0]), int(N[1])
min_sum = 0
for indx, num in enumerate(sleep_awake):
    if num == 1:
        min_sum += theorems[indx]

left = 0
global_max = 0
max_ = 0

for right in range(n):
    if right - left > k-1:
        if sleep_awake[left] == 0:
            max_ -= theorems[left]
        left += 1
    if sleep_awake[right] == 0:
        max_ += theorems[right]
    global_max = max(global_max, max_)
print(global_max + min_sum)
    
    
    