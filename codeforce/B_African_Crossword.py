# Get rows, cols and grid input
rows, cols = list(map(int, input().split()))
grid = []
for row in range(rows):
    string = input()
    grid.append([char for char in string])

# Iterate through grid and find unique characters
string = ''
for row in range(rows):
    for col in range(cols):
        
        curnt_char = grid[row][col] 
        row_chars = grid[row] # chars in curent row
        
        ext_curnt = row_chars[0 : col] # chars in row except current char
        if col + 1 < cols:
            ext_curnt.extend(row_chars[col+1 : cols])
            
        if curnt_char in ext_curnt:
            continue # if char exists in current row no need to check vertically
        
        # check vertically
        char_exist = False
        for sub_row in range(rows):
            if sub_row == row:
                continue
            if curnt_char == grid[sub_row][col]:
                char_exist = True
                break
            
        if not char_exist:
            string += curnt_char
        
print(string)
