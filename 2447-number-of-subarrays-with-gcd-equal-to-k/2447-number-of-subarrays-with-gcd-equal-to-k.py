class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        count = 0
        
        for i in range(len(nums)):
            common_gcd = 0
            
            for j in range(i, len(nums)):
                common_gcd = gcd(common_gcd, nums[j])
                
                if common_gcd == k:
                    count += 1
                elif common_gcd < k:
                    break
                    
        return count