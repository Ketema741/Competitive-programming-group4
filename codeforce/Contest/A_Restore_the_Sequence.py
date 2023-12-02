def solve(nums):
  res = []
  left, right = 0, len(nums) - 1
  """
    0 1 2 3 4 5 6
    3 4 5 2 9 1 1
    ^

  """
  while left <= right:
    res.append(nums[left])

    if left != right:
      res.append(nums[right])

    left += 1
    right -= 1

  return res
    

def main():
    t = int(input())

    for _ in range(t):
      n = int(input())
      nums = list(map(int, input().split()))
      res = solve(nums)
      print(*res)

main()