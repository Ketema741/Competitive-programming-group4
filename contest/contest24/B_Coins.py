num = [0, 0, 0]
temp = [0] * 10

for i in range(3):
    temp = input().strip()
    if temp[1] == '>':
        num[ord(temp[0]) - ord('A')] += 1
    if temp[1] == '<':
        num[ord(temp[2]) - ord('A')] += 1

if num[0] == num[1] or num[1] == num[2] or num[2] == num[0]:
    print("Impossible")
else:
    min_val = mid_val = max_val = 0
    for i in range(3):
        if num[i] == 2:
            max_val = i
        if num[i] == 1:
            mid_val = i
        if num[i] == 0:
            min_val = i
    print(chr(min_val + ord('A')) + chr(mid_val + ord('A')) + chr(max_val + ord('A')))
