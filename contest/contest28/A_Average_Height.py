test_len = int(input())

for  _ in range(test_len):
    n = int(input())
    nums = list(map(int, input().split()))
    odd, even = [], []
    res = []
    for num in nums:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
  
    res.extend(odd)
    res.extend(even)
    print(*res)

            

