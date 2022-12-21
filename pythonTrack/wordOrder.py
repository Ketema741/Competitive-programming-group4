# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
words =[] 
for i in range(n):
    words.append(input().split(" ")[0])
    res = {}
for i in range(len(words)):
    res[words[i]] = 1 + res.get(words[i], 0)
print(len(res))
ans = ' '
for val in res.values():
    ans += str(val) + ' '
print(ans[1:-1])

