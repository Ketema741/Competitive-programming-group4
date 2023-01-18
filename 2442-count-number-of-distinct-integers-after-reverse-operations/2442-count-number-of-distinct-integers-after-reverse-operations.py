class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        res = [num for num in nums]
        for num in nums:
            rev = 0
            
            # reverse the number
            while num > 0:
                rev *= 10
                rev += num % 10
                num  = num // 10
            res.append(rev)
            
        # return the count of distinct integers
        return len(set(res))
