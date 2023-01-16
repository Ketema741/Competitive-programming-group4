class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        mod = 10**9 + 7
        freq = defaultdict(int)
   
        for x in deliciousness: 
            freq[x] += 1
        
        ans = 0
        for x in freq: 
            for k in range(22): 
                if 2**k - x <= x and 2**k - x in freq: 
                    ans += freq[x]*(freq[x]-1)//2 if 2**k - x == x else freq[x]*freq[2**k-x]
        return ans % mod