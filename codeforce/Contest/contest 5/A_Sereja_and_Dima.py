N = int(input())

nums = list(map(int, input().split()))

left, right = 0, N - 1
sereja = dima = 0
turn = 0

while left <= right:
  if turn == 0:
    if nums[left] < nums[right]:
      sereja += nums[right]
      right -= 1
    else:
      sereja += nums[left]
      left += 1
    turn = 1
  else:
    if nums[left] < nums[right]:
      dima += nums[right]
      right -= 1
    else:
      dima += nums[left]
      left += 1
    turn = 0
    
print(sereja, dima)
