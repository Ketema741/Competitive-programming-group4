class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        running_sum = 0
        hash_map = defaultdict(int)
        res = 0

        for num in nums:
            hash_map[running_sum] += 1
            running_sum += num

            diff = running_sum - goal
            res += hash_map[diff]
        
        return res

