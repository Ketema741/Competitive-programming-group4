class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        state = [[0]*n for _ in range(m)]

        for x, y in guards +  walls:
            state[x][y] = 1

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for x, y in guards:
            for dx, dy in directions:
                curr_x, curr_y = x, y

                while 0 <= curr_x + dx < m and 0 <= curr_y + dy < n and state[curr_x + dx][curr_y + dy] != 1:
                    curr_x += dx
                    curr_y += dy
                    state[curr_x][curr_y] = 2

        res = 0
        for i in range(m):
            for j in range(n):
                if state[i][j] == 0:
                    res += 1
        
        return res
