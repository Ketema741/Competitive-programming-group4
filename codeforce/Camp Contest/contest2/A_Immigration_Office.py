from bisect import bisect_left


n = int(input())
people = list(input().split(' '))
k = int(input())
imagPeople  = []
res = []
for _ in range(k):
    imagPeople.append(input())

for name in imagPeople:
    res.append(bisect_left(people, name))
    
for val in res:
    print(val)