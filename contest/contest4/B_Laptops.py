n = int(input())

has_laptops = False
input_laptops = []
for i in range(n):
    a, b = list(input().split())
    input_laptops.append((int(a), int(b)))
    
input_laptops.sort()
for j in range(1, n):
    a, b = input_laptops[j-1]
    c, d = input_laptops[j]
    if b > d:
        has_laptops = True
        break
    if has_laptops:
        break

if has_laptops:
    print("Happy Alex")
else:
    print("Poor Alex")