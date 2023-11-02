class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ptr_one, ptr_two = m - 1, n - 1
        last_indx = m + n - 1
        
        while ptr_one >= 0 and ptr_two >= 0:
            if nums1[ptr_one] > nums2[ptr_two]:
                nums1[last_indx] = nums1[ptr_one]
                ptr_one -= 1
            else:
                nums1[last_indx] = nums2[ptr_two]
                ptr_two -= 1
                
            last_indx -= 1
            
        while ptr_two >= 0:
            nums1[last_indx] = nums2[ptr_two]
            ptr_two -= 1
            last_indx -= 1