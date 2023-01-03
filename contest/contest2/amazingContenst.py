N = int(input())
contests = list(map(int, input().split()))
count = 0
min_ = max_ = contests[0]
for indx in range(1, N):
    if contests[indx] < min_:
        count += 1
        min_ = contests[indx]
    if contests[indx] > max_:
        count += 1   
        max_ = contests[indx]
print(count)        
