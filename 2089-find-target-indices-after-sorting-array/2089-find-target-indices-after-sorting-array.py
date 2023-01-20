class Solution(object):
    def targetIndices(self, nums, target):
        sorted_nums = sorted(nums)
        target_indeces = []
        
        for indx in range(len(nums)):
            if sorted_nums[indx] == target:
                target_indeces.append(indx)
                
        return target_indeces