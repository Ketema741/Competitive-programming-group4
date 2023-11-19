def is_beautiful_array(arr):
    n = len(arr)
    for i in range(2, n):
        if arr[i] == sum(arr[:i]):
            return False
    return True


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Check if the array is already beautiful
    if is_beautiful_array(a):
        print("YES")
        print(' '.join(map(str, a)))
        continue

    # Reorder the elements of the array
    reordered_a = []
    reordered_a.append(a[0])
    for i in range(1, n):
        if a[i] != sum(a[:i]):
            reordered_a.append(a[i])
    
    # Check if the reordered array is beautiful
    if is_beautiful_array(reordered_a):
        print("YES")
        print(' '.join(map(str, reordered_a)))
    else:
        print("NO")
