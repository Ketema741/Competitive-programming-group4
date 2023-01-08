def calculate_shirt_size(shirt):
    hash_map = {'S':1, 'M':2, 'L':3, 'X':4}
    shirt_size = 0
    if len(shirt) > 1:
        for indx in range(len(shirt)-1):
            shirt_size += hash_map[shirt[indx]]
        if shirt[-1] == 'L':
            shirt_size += hash_map['L']
        else:
            shirt_size = hash_map['S'] - shirt_size
    else:
        shirt_size += hash_map[shirt] 
    return shirt_size

N = int(input())
res = []
for inputs in range(N):
    first_tshirt, second_tshirt= input().split()
    size1 = calculate_shirt_size(first_tshirt)
    size2 = calculate_shirt_size(second_tshirt)
    if size1 < size2:
        res.append('<')
    elif size1 > size2:
        res.append('>')
    else:
        res.append('=')
for operator in res:
    print(operator)