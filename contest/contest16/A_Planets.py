test_len = int(input())

for _ in range(test_len):
    n, c = list(map(int, input().split()))

    planets = list(map(int, input().split()))
    hash_map = {}

    for num in planets:
        hash_map[num] = 1 + hash_map.get(num, 0)

    res = 0

    for key, val in hash_map.items():
        if val < c:
            res += val
        else:
            res += c

    print(res)