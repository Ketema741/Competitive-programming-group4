n, d = list(map(int, input().split()))
powers = sorted(list(map(int, input().split())))

count, teams = 0, 1
left, right = 0, len(powers)-1

while left <= right:
    if powers[right]*teams > d:
        count += 1
        teams = 1
        right -= 1
    else:    
        left +=1
        teams += 1
print(count)