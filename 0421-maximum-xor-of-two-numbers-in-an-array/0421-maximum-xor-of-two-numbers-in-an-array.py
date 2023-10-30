class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        # Determine the maximum number of bits needed to represent the numbers
        L = len(bin(max(nums))) - 2
        
        maxXOR = 0
        mask = 0

        for i in range(L - 1, -1, -1):
            mask = (mask << 1) | 1
            prefixSet = set()
            maxXOR <<= 1
            
            for num in nums:
                prefixSet.add(num >> i)
                
            possibleMaxXOR = maxXOR | 1
            
            for prefix in prefixSet:
                if (possibleMaxXOR ^ prefix) in prefixSet:
                    maxXOR |= 1
                    break
        
        return maxXOR
