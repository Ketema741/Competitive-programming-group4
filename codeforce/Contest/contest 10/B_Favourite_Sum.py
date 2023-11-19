test_len = int(input())
sum_ = 0
for _ in range(test_len):
    n, x = map(int, input().split())
    favourites = list(map(int,input().split()))

    sum_ = x*(x+1)//2
    fav = 0
    for num in favourites:
        if num <= x:
            sum_ -= 2*num
    print(sum_)
