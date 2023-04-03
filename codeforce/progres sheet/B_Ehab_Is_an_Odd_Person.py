n = int(input())
ex = [False, False]
arr = list(map(int, input().split()))

for i in range(n):
    ex[arr[i] % 2] = True

if ex[0] and ex[1]:
    arr.sort()

print(*arr)
