len_test  = int(input())
res = []
nums_temp =[]

for indx in range(len_test):
    len_input = int(input())
    nums = list(input().split())
    nums_temp.clear()
    nums_temp.extend(nums)
    strings = list(input())
    for str_indx, char in enumerate(strings):
        for num_indx in range(str_indx, len_input):
            if nums_temp[num_indx].isdigit() and nums[num_indx] == nums[str_indx]: 
                nums_temp[num_indx] = char 
    if nums_temp == strings:
        res.append('YES')
    else:
        res.append('NO')
for ans in res:
    print(ans)