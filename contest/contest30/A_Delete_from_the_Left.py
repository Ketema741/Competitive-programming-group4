s = input()
t = input()

l1 = len(s)
l2 = len(t)
length = l1 + l2
c = 0

if s[l1 - 1] != t[l2 - 1]:
    print(length)
else:
    l1 -= 1
    l2 -= 1
    while l1 >= 0 and l2 >= 0:
        if s[l1] == t[l2]:
            c += 1
            l1 -= 1
            l2 -= 1
        elif s[l1] != t[l2]:
            break
    print(length - (c * 2))
