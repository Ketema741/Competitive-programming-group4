N = int(input())

for i in range(N):
    l1, w1 = map(int, input().split())
    l2, w2 = map(int, input().split())
    
    min_1 = min(l1, w1)
    min_2 = min(l2, w2)
    min_sum = min_1 + min_2
    if min_sum == max(l1, w1) or min_sum == max(l2, w2):
        print("YES")
    else:
        print("NO")