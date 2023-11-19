def recursive(res, bucket, left, right, n):
    if left == right:
        return 
    
    for i in range(left, right):
        bucket.append(n**i)
        res.append(sum(bucket))

        recursive(res, bucket, i + 1, right, n)
        bucket.pop()


test_len = int(input())

mod = 10**9+7

for _ in range(test_len):
    n, k = list(map(int, input().split()))

    k = bin(k)

    res = 0

    i = N = len(k) - 1
    while k[i] != 'b':
        if k[i] == '1':
            res += n**(N - i)
            
        i -= 1
    print(res%mod)    


