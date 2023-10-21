class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hash1, hash2 = set(), set()
        res1, res2 = set(), set()
        for num in nums1:
            hash1.add(num)

        for num in nums2:
            if num not in hash1:
                res2.add(num)
            hash2.add(num)
            
        for num in nums1:
            if num not in hash2:
                res1.add(num)


        return [list(res1), list(res2)]