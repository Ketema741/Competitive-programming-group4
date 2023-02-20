n, m = list(map(int, input().split()))

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
res = []

right = left = 0
while left in range(m):
    while right < n and arr2[left] > arr1[right] :
        right += 1
    
    res.append(right)
    left += 1
    
print(*res)