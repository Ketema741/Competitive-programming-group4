test_len = int(input())

for i in range(test_len):
    num = int(input())

    bin_ = bin(num)
    len_ = right = len(bin_) - 1
    min_positive = 1
    
    while bin_[right] != 'b':
        if bin_[right] == '1':
            break
        right -= 1 

    if bin_[right] == '1':    
        min_positive = 2**(len_ - right)

    while True:
        if (num^min_positive) > 0 and (num&min_positive) > 0:
            print(min_positive)
            break
        else:
            min_positive += 1