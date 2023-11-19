t = int(input())  

for _ in range(t):
    s = int(input()) 
    digits = []
    for i in range(9, 0, -1):
        if s >= i:
            digits.append(i)
            s -= i
    digits = digits[::-1]
    result = int(''.join(map(str, digits)))
    print(result)
