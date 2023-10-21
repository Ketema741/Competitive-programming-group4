class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hash1, hash2 = set(nums1), set(nums2)
        res1, res2 = [], []
      
        for num in hash1:
            if num not in hash2:
                res1.append(num)
            
        for num in hash2:
            if num not in hash1:
                res2.append(num)

        return [res1, res2]