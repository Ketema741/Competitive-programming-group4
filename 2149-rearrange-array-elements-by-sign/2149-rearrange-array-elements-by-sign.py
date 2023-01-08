class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        result =[0] * N
        indx_pos = 0
        indx_neg = 1
        for num in nums:
            if num > 0:
                result[indx_pos] = num
                indx_pos += 2
            else:
                result[indx_neg] = num
                indx_neg += 2   
        return result