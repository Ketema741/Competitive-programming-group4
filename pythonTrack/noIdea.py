from collections import Counter
n, m = input().split()
n = int(n)
m = int(m)

numbers = [int(x) for x in input().split()]
number_count = Counter(numbers)

A=[int(x) for x in input().split()]
B=[int(x) for x in input().split()]

happiness_count = 0

for i in A:
    happiness_count += number_count.get(i,0) 
     
for i in B:
   happiness_count -= number_count.get(i,0)  
   
print(happiness_count) 