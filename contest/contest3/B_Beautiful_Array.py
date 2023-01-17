import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
set_a = []  # - number
set_b = []  # + number
set_c = [0]
for num in arr:
    if num < 0:
        set_a.append(num)
    elif num > 0:
        set_b.append(num)

if len(set_a) % 2 == 0:
    if len(set_b) > 0:
        set_c.append(set_a.pop())
    else:
        set_b.append(set_a.pop())
        set_b.append(set_a.pop())
        set_c.append(set_a.pop())        
else:
    if len(set_b) == 0:
        set_b.append(set_a.pop())
        set_b.append(set_a.pop())
        
print(len(set_a), end=' ')
for num in set_a:
    print(num, end=' ')
print()

print(len(set_b), end=' ')
for num in set_b:
    print(num, end=' ')
print()

print(len(set_c), end=' ')
for num in set_c:
    print(num, end=' ')