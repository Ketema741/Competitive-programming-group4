t = int(input()) 

while t > 0:
    n = int(input())

    if n == 3:
        print(-1)
    else:
        for i in range(n, n - n // 2, -1):
            print(i, end=' ')
        for i in range(1, n // 2 + 1) if n % 2 == 0 else range(1, n // 2 + 2):
            print(i, end=' ')
        print()

    t -= 1
