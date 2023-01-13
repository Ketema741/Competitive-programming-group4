N = int(input())
res = []
members = []
members = input().split()
    
for member in members:
    count = set()
    for char in member:
        count.add(char)
    if len(count) != len(member):
        continue
    res.append(member)
    
flaged_members = input().split()
for flaged in flaged_members:
    if flaged in res:
        res.remove(flaged)
        
print(len(res))