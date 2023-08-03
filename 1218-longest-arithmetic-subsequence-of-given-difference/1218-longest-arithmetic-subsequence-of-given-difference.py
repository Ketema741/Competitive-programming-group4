class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = {}
        
        for num in arr:
            subElement = num - difference
            
            if subElement in memo:
                memo[num] = 1 + memo[subElement]
            else:
                memo[num] = 1
                
        return max(memo.values())