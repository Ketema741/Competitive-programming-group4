def divideAndConquer(left, right, arr):
    if right - left == 1:
        return 0
    
    mid = (left + right) // 2
    left_max = max(arr[left:mid])
    right_max = max(arr[mid:right])

    curr_count = 0
    if left_max > right_max:
        curr_count += 1
        arr[left:mid], arr[mid:right] = arr[mid:right], arr[left:mid]

    left_count = divideAndConquer(left, mid, arr)
    right_count = divideAndConquer(mid, right, arr)
    
    return left_count + right_count  + curr_count

def solve_case(m, arr):
    count = divideAndConquer(0, m, arr)
    if arr == sorted(arr):
        return count
    
    return -1

test_len = int(input())
for _ in range(test_len):
    m = int(input())
    arr = list(map(int, input().split()))
    print(solve_case(m, arr))