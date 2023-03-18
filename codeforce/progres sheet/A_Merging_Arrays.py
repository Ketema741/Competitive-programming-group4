n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))


left1, left2 = 0, 0
res = []
while left1 < n and left2 < m:
    if arr1[left1] > arr2[left2]:
        res.append(arr2[left2])
        left2 += 1
    else:
        res.append(arr1[left1])
        left1 += 1
    if left1 == n:
        res.extend(arr2[left2:])
        break
    if left2 == m:
        res.extend(arr1[left1:])
        break
    
print(*res)