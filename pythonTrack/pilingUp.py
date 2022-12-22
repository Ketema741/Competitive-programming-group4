# Enter your code here. Read input from STDIN. Print output to STDOUT
stack, res = [], []

def PilingUp(n, blocks):
    left, right = 0, n - 1
    if blocks[left] > blocks[right] and len(stack) == 0:
        stack.append(blocks[left]) 
    elif blocks[left] < blocks[right] and len(stack) == 0:
        stack.append(blocks[right])
           
    while left < right:
        if blocks[left] > blocks[right]:
            if stack[-1] < blocks[left]:
                res.append("No")
                break
            left +=    1
        else:
            if stack[-1] < blocks[right]:
                res.append("No")
                break
            right -= 1
    res.append("Yes")
    
    

T = int(input('T: '))
for i in range(T):
    n = int(input('N: '))
    blocks = input("B: ").split(" ")
    PilingUp(len(blocks), blocks)
    
    
for ans in res:
    print(ans)
 
        

"""

0  1  2  3  4  5 
1  2  3  4  8  7

"""