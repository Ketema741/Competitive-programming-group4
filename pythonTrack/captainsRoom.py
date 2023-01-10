# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
k=int(input()) 
rooms =map(int, input().split())
hash_map = Counter(rooms) 
for k,v in hash_map.items():
    if v == 1:
        print(k)
        break