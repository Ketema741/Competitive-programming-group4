import heapq


test_len = int(input())

for _ in range(test_len):
    n, m = list(map(int, input().split()))
    nums1 =list(map(int, input().split())) 
    nums2 =list(map(int, input().split())) 

    heapq.heapify(nums1)

    i = 0
    while m != i:
        heapq.heappop(nums1)
        heapq.heappush(nums1, nums2[i])
        i += 1

    print(sum(nums1))