class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left_nums = []
        right_nums = []
        pivot_count = 0
        
        for num in nums:
            if num < pivot:
                left_nums.append(num)
            elif num > pivot:
                right_nums.append(num)
            else:
                pivot_count += 1
        for i in range(pivot_count):
            left_nums.append(pivot)
        left_nums.extend(right_nums)
        return left_nums
                