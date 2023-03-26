class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr = [0] * (len(nums) + 1)
        dup, missing = -1, 1
        for i in range(len(nums)):
            arr[nums[i]] += 1
        for i in range(1, len(arr)):
            if arr[i] == 0:
                missing = i
            elif arr[i] == 2:
                dup = i
        return [dup, missing]
