class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums2 = [0] * k
        
        while k:
            nums2[k-1] = nums.pop()
            k -= 1
            
        for num in nums2[::-1]:
            nums.insert(0,num)