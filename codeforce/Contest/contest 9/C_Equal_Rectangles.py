t = int(input())

for _ in range(t):
    n = int(input())
    all_sides = sorted(list(map(int,input().split())))
   
    i, j = 0, len(all_sides) - 1
    is_true = True
    area = all_sides[i] * all_sides[j]

    while i < j:
        sub_area = all_sides[i] * all_sides[j]

        if sub_area != area:
            is_true = False
            break
        
        if all_sides[i+1] != all_sides[i] or all_sides[j] != all_sides[j-1]:
            is_true = False
            break

        i += 2
        j -= 2

    if is_true:
        print("YES")
    else:
        print("NO")