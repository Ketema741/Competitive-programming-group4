N  = int(input())
scores = input().split()
count = 0
stack = []
stack.append(scores[0])
min_ = scores[0]
max_ = scores[0]
for indx  in range(1, len(scores)):
    if scores[indx] > max_ :
        count += 1 
    elif scores[indx] < min_:
        count += 1 
    max_ = max(max_, scores[indx])
    min_ = min(min_, scores[indx])

print(count)