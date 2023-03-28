class Solution:
    def findKthLargest (self, nums: List[int], k: int) -> int: 
        k = len(nums) - k
        
        def quickSelect(left: int, right: int) -> int:
            while True:
                pivot = right
                write = left

                for read in range(left, right):
                    if nums[read] <= nums[pivot]:
                        nums[write], nums[read] = nums[read], nums[write]
                        write += 1

                nums[write], nums[pivot] = nums[pivot], nums[write]

                if write == k:
                    return nums[write]
                elif write > k:
                    right = write - 1
                else:
                    left = write + 1

            
        return quickSelect(0, len (nums) - 1)
    