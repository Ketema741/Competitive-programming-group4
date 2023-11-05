class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)

        q = deque([num for num in arr])

        while True:
            count = 0

            if q[0] < q[1]:
                q[0], q[1] = q[1], q[0]
            
            while q[0] > q[1]:
                count += 1
                q[0], q[1] = q[1], q[0]
                q.append(q.popleft())

                if count >= k:
                    return q[0]