from collections import deque


test_len = int(input())


for _ in range(test_len):
    n = int(input())
    nums = list(map(int, input().split()))
    queue = deque([])

    for i in range(len(nums)):
        queue.append(nums[i])

    res = []
    while n:
        current  = queue.popleft() 
        xor = queue[0] 
        for i in range(1, len(queue)):
            xor = xor ^queue[i]

        if xor == current:
            print(current)
            break
        n -= 1    
        queue.append(current)