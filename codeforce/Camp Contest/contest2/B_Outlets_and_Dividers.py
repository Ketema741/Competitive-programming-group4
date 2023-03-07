test_len = int(input())

for _ in range(test_len):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    sum_ = 2
    possible = False
    for i in range(m):
        if n <= 2:
            print(0)
            possible = True
            break

        sum_ += arr[i] - 1

        if sum_ >= n:
            print(i+1)
            possible = True
            break

    if not possible:
        print(-1)