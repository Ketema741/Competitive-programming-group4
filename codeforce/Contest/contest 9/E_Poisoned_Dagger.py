t = int(input())

for _ in range(t):
    n, h = list(map(int, input().split()))
    attack = list(map(int, input().split()))

    left, right = 1, h
    
    while left <= right:
        k = left + (right - left)//2
        attack_sum = 0

        for i in range(1, n):
            attack_sum += min(k, attack[i] - attack[i-1])
        attack_sum += k  

        if attack_sum < h:
            left = k + 1
        else:
            right = k - 1 

    print(left)

