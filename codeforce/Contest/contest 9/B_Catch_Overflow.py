
n = int(input())
stack = []
x = 0

for i in range(n):
    commands = input().strip()
    if commands == 'add':
        x += 1 
    elif "f" == commands[0]:
        n = int(commands[4:])
        stack.append((n, x))
    elif commands == 'end':
        count, start = stack.pop()
        x = start + count * (x - start)
        
if x < 2**32:
    print(x)
else:    
    print('OVERFLOW!!!')
