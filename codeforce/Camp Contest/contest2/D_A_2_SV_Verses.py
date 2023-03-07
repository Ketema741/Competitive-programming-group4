n, start, end = map(int, input().split())
arr = list(map(int, input().split()))


def subArraySum(arr, k):
    count = 0
    left = 0
    sub_sum = 0
    for right in range(len(arr)):
        sub_sum += arr[right]
      
        while sub_sum >= k:
            sub_sum -= arr[left]
            left += 1
        count += right - left + 1
    return count

print(subArraySum(arr, end + 1) - subArraySum(arr, start))
