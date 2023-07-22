class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        count = 0
        
        def merge(left, right):
            nonlocal count
            res  = []
            
            p1, n1_len = 0, len(left)
            p2, n2_len = 0, len(right)
            
            while p1 < n1_len and p2 < n2_len:
                if left[p1] <= right[p2] + diff:
                    count += n2_len - p2
                    p1 += 1
                else:
                    p2 += 1
            
            p1 = p2 = 0 
            while p1 < n1_len and p2 < n2_len:
                if left[p1] < right[p2]:
                    res.append(left[p1])
                    p1 += 1
                else:
                    res.append(right[p2])
                    p2 += 1
                    
            res.extend(left[p1:])
            res.extend(right[p2:])
            
            return res
            
        def partition(nums):
            if len(nums) == 1:
                return nums
            
            mid = len(nums) // 2
            
            num_left = partition(nums[:mid])
            num_right = partition(nums[mid:])
            
            return merge(num_left, num_right)
            
        nums = [nums1[i] - nums2[i] for i in range(len(nums1))]
        
        partition(nums)  
    
        return count