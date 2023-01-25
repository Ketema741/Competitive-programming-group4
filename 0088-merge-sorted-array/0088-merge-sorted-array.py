class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        pointr_one, pointr_two = m - 1, n - 1
        last_indx = m + n - 1
        
        while pointr_one >= 0 and pointr_two >= 0:
            if nums1[pointr_one] > nums2[pointr_two]:
                nums1[last_indx] = nums1[pointr_one]
                pointr_one -= 1
            else:
                nums1[last_indx] = nums2[pointr_two]
                pointr_two -= 1
                
            last_indx -= 1
            
        while pointr_two >= 0:
            nums1[last_indx] = nums2[pointr_two]
            pointr_two -= 1
            last_indx -= 1