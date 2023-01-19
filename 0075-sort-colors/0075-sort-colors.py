class Solution(object):
    def sortColors(self, nums):
        # Count the occurrence of each color
        color_count = [0] * 3
      

        for i in range(len(nums)):
            color_count[nums[i]] += 1
        
        current_index = 0 # Keep track of the current index in the nums list
        
        # Iterate through the color_count array and 
        # add the appropriate number of each color to the nums list
        for i in range(3):
            for j in range(color_count[i]):  
                nums[current_index] = i
                current_index += 1
        return nums