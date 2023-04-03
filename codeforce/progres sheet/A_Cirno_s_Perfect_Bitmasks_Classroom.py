test_len = int(input())

for i in range(test_len):
    num = int(input())

    min_pos = num&-num
    while True:
        if (num^min_pos) > 0 and (num&min_pos) > 0:
            print(min_pos)
            break
        else:
            min_pos += 1