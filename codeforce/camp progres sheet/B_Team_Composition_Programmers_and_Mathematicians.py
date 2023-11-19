test_len = int(input())

for _ in range(test_len):
    a, b = map(int, input().split())
    print(min(min(a, b), (a + b)//4))