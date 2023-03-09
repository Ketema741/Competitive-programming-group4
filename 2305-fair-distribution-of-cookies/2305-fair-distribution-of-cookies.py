class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0]*k
        pre_min = float('inf')
        
        def backtrack(i):
            nonlocal pre_min
            if i >= len(cookies):
                return max(bucket)
            
            if max(bucket) > pre_min:
                return pre_min
            
            for j in range(k):
                if bucket[j] + cookies[i] < pre_min:
                    bucket[j] += cookies[i]
                    current_min = backtrack(i+1)
                    pre_min = min(pre_min, current_min)
                    bucket[j] -= cookies[i]
            return pre_min
        
        return backtrack(0)
                