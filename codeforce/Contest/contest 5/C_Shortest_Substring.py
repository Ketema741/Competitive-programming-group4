from collections import defaultdict


N = int(input())
res = []

for _ in range(N):
  nums = input()

  hash_map= defaultdict(int)
  left, right = 0, 0
  min_window = float("inf")

  while right < len(nums):
    hash_map[nums[right]] += 1

    while len(hash_map) == 3:
      min_window = min(min_window, right - left + 1)
      hash_map[nums[left]] -= 1

      if hash_map[nums[left]] == 0:
        hash_map.pop(nums[left])
      left += 1

    right += 1
    
  min_window = min_window if min_window != float("inf") else 0
  res.append(min_window)

for ans in res:
  print(ans)


