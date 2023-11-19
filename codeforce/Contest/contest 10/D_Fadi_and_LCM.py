n = int(input())

def gcd(a, b):
    if b == 0: return a

    gcd(b, b%a)

    for i in range(x):