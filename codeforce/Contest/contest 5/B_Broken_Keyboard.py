tests = int(input())
for _ in range(tests):
    string = input()
    size = len(string)
    left = 0
    res = set()
    
    while left < size:
        right = left + 1
        count = 1
        while right < size and string[right] == string[left]:
            count += 1
            right += 1
            left += 1

        if count % 2 != 0:
            res.add(string[left])

        left += 1

    res = sorted(list(res))
    print("".join(res))