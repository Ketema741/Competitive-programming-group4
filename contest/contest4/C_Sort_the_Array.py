n = int(input())

arr = list(map(int, input().split()))

sorted_arr = sorted(arr)
indeces = []
if sorted_arr != arr:
    for indx, num in enumerate(sorted_arr):
        if num != arr[indx]:
            if len(indeces) > 1:
                indeces.pop()
                indeces.append(indx)
            else:
                indeces.append(indx)
    reversed_arr = reversed(arr[indeces[0]:indeces[-1] + 1])
    
    new_arr = arr[0:indeces[0]] 
    new_arr.extend(reversed_arr)
    new_arr.extend(arr[indeces[-1] + 1:])
    
    if new_arr == sorted_arr:
        print("yes")
        print(indeces[0] + 1, indeces[-1] + 1)
    else:
        print("no")
else:
    print("yes")
    print(1, 1)