stones = input().split()

res = set()
for stone in stones:
    res.add(stone) 
if len(res) >= 5:
    print("YES")
else: 
    print("NO")
