N = int(input())

res = []
for i in range(N):
    word = input()
    res.append(word)
for word in res:
    ouput =  word[:2] +"... " + word[:] +"?"
    print(ouput)
