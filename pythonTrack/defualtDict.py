# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

N, M = map(int, input().split())
A = []
B = []
res = defaultdict(list)
for indx in range(N):
    A.append(input())
for indx in range(M):
    B.append(input())
    
for indx, char in enumerate(A):
    res[char].append(str(indx+1))
for char in B:
    if char in res:
        print(' '.join(res[char]))
    else:
        print('-1')