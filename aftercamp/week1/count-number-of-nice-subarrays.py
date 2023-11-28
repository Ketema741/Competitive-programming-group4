class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
                
        prefix_sum = defaultdict(int)
        prefix_sum[0] += 1

        cur_sum = 0
        res = 0
        
        for num in nums:
            cur_sum += num
            diff = cur_sum - k
            res += prefix_sum[diff]
            prefix_sum[cur_sum] += 1
            
        return res
    
    """
        1 1 2 1 1
        1 1 0 1 1
                ^

        sum = 0  count = 0  0:1
        sum = 1  count = 0  1: 1
        sum = 2  count = 1  2: 1
        sum = 2  count = 2  2: 2
        sum = 3  count = 3  3: 1
        sum = 4  count = 5  4: 1

    """