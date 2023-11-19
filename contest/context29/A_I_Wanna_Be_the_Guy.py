def can_pass_all_levels(n, p_levels, q_levels):
    all_levels = set(range(1, n+1))  
    
    x_levels = set(p_levels[1:])  
    y_levels = set(q_levels[1:])  
    
    combined_levels = x_levels.union(y_levels)  
    
    return "I become the guy." if combined_levels == all_levels else "Oh, my keyboard!"

n = int(input())
p_levels = list(map(int, input().split()))
q_levels = list(map(int, input().split()))

result = can_pass_all_levels(n, p_levels, q_levels)

print(result)
