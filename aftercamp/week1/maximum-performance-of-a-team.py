class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        pairs = [(eff, spd) for eff, spd in zip(efficiency, speed)]
        pairs.sort(reverse=True)
        mod = 10 ** 9 + 7
        min_heap = []
        res, tot_speed = 0, 0

        for eff, spd in pairs:
            if len(min_heap) == k:
               val = heapq.heappop(min_heap)
               tot_speed -= val

            tot_speed += spd
            res = max(res, tot_speed * eff)
            heapq.heappush(min_heap, spd)
        
        return res % mod

        