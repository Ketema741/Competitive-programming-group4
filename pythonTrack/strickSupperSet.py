# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(input().split())
n = int(input())
sets = []
ans = True
for i in range(n):
    sets.append(set(input().split()))
    
for set_ in sets:
    if A.issuperset(set_):
        continue 
    else:
        ans= False
        break
print(ans) 

