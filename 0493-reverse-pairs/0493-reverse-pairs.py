class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = 0
        
        def mergeSort(arr1, arr2):
            nonlocal count
            res = []
            
            ptr1 = 0
            ptr2 = 0
            
            while ptr1 < len(arr1) and ptr2 < len(arr2):
                
                if arr1[ptr1] > 2*arr2[ptr2]:
                    ptr1 += 1
                    count += len(arr2) - (ptr2)
                else: 
                    ptr2 += 1
                
            ptr1 = ptr2 = 0

            while ptr1 < len(arr1) and ptr2 < len(arr2):
                if arr1[ptr1] > arr2[ptr2]:
                    res.append(arr1[ptr1])
                    ptr1 += 1
                else:
                    res.append(arr2[ptr2])
                    ptr2 += 1
                    
            res.extend(arr1[ptr1:])
            res.extend(arr2[ptr2:])
            
            return res
            
        def partition(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums)//2
            
            left_arr = partition(nums[:mid])
            right_arr = partition(nums[mid:])
            
            return mergeSort(left_arr, right_arr)
            
        partition(nums)  
        return count