n, k, q = list(map(int, input().split()))

res, recipes = [], {}
min_ , max_ = 0, 0
for _ in range(n):
    start, end = list(map(int, input().split()))
    min_ = min(min_, start)
    max_ = max(max_, end)
    while start <= end:
        recipes[start] = 1 + recipes.get(start, 0)
        start += 1
for key, val in recipes.items():
    if val >= k:
        recipes[key] = 1
    else:
        recipes[key] = 0
sum_ = 0  
for key, val in recipes.items():
    sum_ += val
    recipes[key] = sum_

for _ in range(q):
    admissible = 0
    start, end = list(map(int, input().split()))
    if end in recipes:
        admissible = abs(recipes.get(end, 0) - recipes.get(start - 1, 0))
    
    if start not in recipes and end not in recipes:
        if end >= max_ and start <= max_:
            admissible = recipes.get(max_, 0)
        elif end < min_ or start > max_:
            admissible = 0
        else:
            admissible = recipes.get(min_, 0)
    res.append(admissible)

for num in res:
    print(num)
