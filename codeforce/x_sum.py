from collections import defaultdict

test_num = int(input())

for _ in range(test_num):
    # take the input
    input_ = []
    rows, cols = list(map(int, input().split(' ')))
    max_ = 0
    for _ in range(rows):
        cell = list(map(int, input().split()))
        input_.append(cell)
    
    # elements on the diagonal have the same col-row for forward diagonal or 
    # col + row for backward diagonal
    sum_hash_map = defaultdict(int) # the same row + col
    diff_hash_map = defaultdict(int) # the same row - col
    res = []
    for row in range(rows):
        for col in range(cols):
            diff_hash_map[col- row] += input_[row][col]
            sum_hash_map[col + row] += input_[row][col] 
    # calculate diagonal sum at a given point buy adding  forward and backward diagonal 
    for row in range(rows):
        for col in range(cols):
            sum_ = diff_hash_map[(col-row)] + sum_hash_map[(col+row)] - input_[row][col]
            max_ = max(max_, sum_)
    print(max_)