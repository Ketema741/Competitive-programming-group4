from collections import Counter

test_len = int(input())
res = []
for indx in range(test_len):
    planet_len, second_Pcost = list(map(int, input().split()))
    
    orbits = Counter(map(int, input().split()))
   
    pus_count = 0
    #counting the total cost of destroying all the planets
    for key, value in orbits.items():
        if value >= second_Pcost:
            pus_count += second_Pcost
        else:
            pus_count += value
    res.append(pus_count)
for cost in res:
    print(cost)