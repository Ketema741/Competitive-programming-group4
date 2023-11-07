class Solution:
    def numTeams(self, ratings: List[int]) -> int:
        upper_cache = [0 for _ in range(len(ratings))]
        lower_cache = [0 for _ in range(len(ratings))]
        
        res = 0
        for i in range(len(ratings)):
            for j in range(i):
                if ratings[j] < ratings[i]:
                    res += upper_cache[j]
                    upper_cache[i] += 1
                else:
                    res += lower_cache[j]
                    lower_cache[i] += 1
                    
        return res