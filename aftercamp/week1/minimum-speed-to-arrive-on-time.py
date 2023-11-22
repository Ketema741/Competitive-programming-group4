class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def check(speed):
            hours = 0
            N = len(dist)

            for i in range(N):
                if i != N - 1:
                    hours += ceil(dist[i] / speed)
                else:
                    hours += dist[i] / speed
            return hours <= hour
        
        left, right = 1, 10**9 + 1
        res = -1
        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                right = mid - 1
                res = mid
            else:
                left = mid + 1
        
        return left if res != -1 else -1

    """
    
    [10, 20] hour = 2
      0    1
      mid = 1000
    check(10)
    hours = 1 + 2

    l = 11, r = 20
    mid = 15

    l = 16 , r = 20
    mid = 18

    l = 19 r = 20
    mid = 19
    l = 20 r 20 
    mid = 20
    l = 20, r = 19


    """
