from collections import defaultdict
import math


n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
res = left = 0
hash_map = defaultdict()

for right in range(n):
    hash_map[nums[right]] = 1 + hash_map.get(nums[right], 0)
    
    while len(hash_map) > k:
        hash_map[nums[left]] -= 1
        
        if hash_map[nums[left]] == 0:
            hash_map.pop(nums[left])
        left += 1
    res +=   right - left +1
        
print(res)