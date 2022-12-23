class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        x, y = m - 1, n - 1
        last = m + n - 1
        while x >= 0 and y >= 0:
            if nums1[x] > nums2[y]:
                nums1[last] = nums1[x]
                x -= 1
            else:
                nums1[last] = nums2[y]
                y -= 1
            last -= 1
        while y >= 0:
            nums1[last] = nums2[y]
            y -= 1
            last -= 1
        """
        Do not return anything, modify nums1 in-place instead.
        """
        