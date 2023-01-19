class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        nums_len = len(nums)
        count = [0] * nums_len

        # Iterate through the list of nums
        for indx_i in range(nums_len):
            
            # Compare the current element with all other elements in the list
            for indx_j in range(nums_len):
                if nums[indx_i] > nums[indx_j]:
                    # Increment the count for the current element
                    count[indx_i] += 1
        # Return the count list
        return count