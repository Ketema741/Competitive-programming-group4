def solve():
    n , k = map(int , input().split())
    nums = list(map(int, input().split()))
    
    left = 0
    right = 1
    found = False
    nums.sort()
    while right < n:
        difference = nums[right] - nums[left]
        if difference == k:
             found = True
             break
        elif difference > k:
              left += 1
        else:
              right += 1
    
    if found:
        print("YES")
    else:
        print("NO")
        
def main():
    t = int(input())
    
    for _ in range(t):
        solve()

main()


