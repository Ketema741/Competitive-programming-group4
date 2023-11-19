n = int(input())
visited = set()
currState = 0
res = 0

for _ in range(n):
    sign, record = input().split()
    record = int(record)

    if sign == '+':
        visited.add(record)
        currState += 1
        res = max(res, currState)
    else:
        if record in visited:
            visited.remove(record)
            currState -= 1
        else:
            res += 1

print(res)
