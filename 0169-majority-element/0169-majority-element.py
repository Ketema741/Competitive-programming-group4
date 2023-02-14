class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, maxCount = 0, 0
        hash_map = {}
        
        for num in nums:
            hash_map[num] = 1 + hash_map.get(num, 0)
            
            if hash_map[num] > maxCount:
                res = num
            
            maxCount = max(maxCount, hash_map[num])
                
        return res