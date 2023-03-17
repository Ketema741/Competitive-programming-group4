n= int(input())
nums = list(map(int, input().split()))

preSum = []
postSum = [0] * n
sum_ = 0

for num in nums:
    sum_ += num
    preSum.append(sum_)
sum_ = 0  
for indx  in range(n-1,-1,-1):
    sum_ += nums[indx]
    postSum[indx] = sum_

left = 0
right = n - 1

while right > left+1 :
    if preSum[left] > postSum[right]:
        right -= 1
    else:
        left += 1
if len(nums) == 1:
    print(1, 0)
else:
    print(left+1, n - right)
    