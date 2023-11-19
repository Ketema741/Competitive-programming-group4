test_len = int(input())

for _ in range(test_len):
    l, r = map(int, input().split())
    res = []
    for x in range(l, r+1):
        if x*2 <= r:
            res.append((x, x*2))
            
        if len(res) == 1:
            break

        for y in range(x+1, r+1):
            if x != y and y % x == 0:
                res.append((x,y))
                break
        

    print(*res[0])