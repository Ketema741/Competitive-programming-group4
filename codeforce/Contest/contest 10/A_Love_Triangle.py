n = int(input())
likes = list(map(int, input().split()))

for i in range(n):
    first = i+1
    second = likes[i]
    third = likes[second-1]
    forth = likes[third-1]
    if first != second != third and first == forth:
        print("YES")
        break
else:
    print("NO")
