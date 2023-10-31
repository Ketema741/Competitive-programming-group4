class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        res = []
        for indx,num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
               
                return [hash_map[diff], indx]
            hash_map[num] = indx
        