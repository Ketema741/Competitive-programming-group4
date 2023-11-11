class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def isValid(threshold):
            i, count = 0, 0

            while i < len(nums) - 1:
                if (nums[i + 1] - nums[i]) <= threshold:
                    i += 2
                    count += 1
                else:
                    i += 1
                
                if count == p:
                    return True
            return False
        

        left, right = 0, 10**9
        res = 0
        

        nums.sort()

        while left <= right:
            mid = left + (right - left)//2

            if isValid(mid):
                right = mid - 1
                res = mid
            else:
                left = mid + 1

        return res
                
