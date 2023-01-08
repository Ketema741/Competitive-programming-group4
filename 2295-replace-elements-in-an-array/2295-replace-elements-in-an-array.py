class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        res = defaultdict()
        hash_map = {num: i for i, num in enumerate(nums)}
        for old, current in operations:
            indx = hash_map[old]
            nums[indx] = current
            hash_map[current] = indx
            del hash_map[old]
        return nums