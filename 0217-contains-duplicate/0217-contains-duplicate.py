class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = defaultdict(int)
        
        for num in nums:
            hash_map[num] += 1
        
        return len(hash_map) != len(nums)
        