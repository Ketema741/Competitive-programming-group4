
def fact(n):
    factorization = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            factorization.add(d)
            n //= d
        d += 1
        
    if n > 1:
        factorization.add(n)
    
    return len(factorization)

num = int(input())
count = 0

for i in range(1, num+1):
    if fact(i) == 2:
        count += 1
print(count)        