from bisect import bisect_right, bisect_left

def solve(n, l, r, arr):
    arr.sort()  

    pairs_count = 0
    for i in range(n):
        upper_bound = bisect_right(arr, r - arr[i], lo=i + 1)
        lower_bound = bisect_left(arr, l - arr[i], lo=i + 1) 

        pairs_count += max(0, upper_bound - lower_bound)  

    return pairs_count


t = int(input())
for _ in range(t):
    n, l, r = map(int, input().split())
    array = list(map(int, input().split()))

    result = solve(n, l, r, array)
    print(result)
