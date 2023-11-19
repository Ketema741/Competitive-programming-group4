class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        time_frame = -1
        for i in range(len(nums)):

            if nums[i] == 1:
                if i <= time_frame:
                    return False

                time_frame = i + k

        return True
                
