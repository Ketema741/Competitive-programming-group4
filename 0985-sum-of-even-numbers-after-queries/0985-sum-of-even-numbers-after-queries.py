class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        even_sum = 0
        for num in nums:
            if num%2 == 0:
                even_sum += num
                
        for val, indx in queries: 
            if nums[indx] % 2 == 0:
                if (nums[indx]+ val) % 2 == 0:
                    even_sum += val
                else:
                    even_sum -= nums[indx]
            elif (nums[indx]+ val) % 2 == 0:
                even_sum += val + nums[indx]
                
            nums[indx] += val
            result.append(even_sum)
        return result
        
        