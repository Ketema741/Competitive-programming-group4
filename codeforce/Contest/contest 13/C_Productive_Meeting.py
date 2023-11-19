import heapq


test_len = int(input())

for _ in range(test_len):
    curn_talk = 0
    n = int(input())
    nums = list(map(int, input().split()))
    maxHeap = []

    for i, num in enumerate(nums):
        if num > 0:
            maxHeap.append((-num, i))

    heapq.heapify(maxHeap)
    res = []

    while len(maxHeap) > 1:
        num1, i = heapq.heappop(maxHeap)
        num2, j = heapq.heappop(maxHeap)
        res.append((i+1, j+1)) 

        num1 = -num1 - 1 
        num2 = -num2 - 1

        if num1:
            heapq.heappush(maxHeap,(-num1, i))
        if num2:
            heapq.heappush(maxHeap, (-num2, j))
        curn_talk += 1

    print(curn_talk)
    for pair in res:
        print(*pair)

