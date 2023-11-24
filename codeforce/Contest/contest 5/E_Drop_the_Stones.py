def solve():
    r, c = map(int, input().split())
    grid = []

    for _ in range(r):
        rows = list(input())
        grid.append(rows)
        
    for col in range(c):
        cur = r
        for row in range(r - 1, -1, -1):
            if grid[row][col] == "*":
                cur -= 1

                if cur != row:
                    grid[cur][col] = "*"
                    grid[row][col] = "."

            elif grid[row][col] == "o":
                cur = row

    for row in range(r):
        for col in range(c):
            print(grid[row][col],end='')
        print()
    print()



def main():
    t = int(input())
    
    for _ in range(t):
        solve()

main()