# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        N = mountain_arr.length()

        l, r = 1, N - 2

        # find peak
        while l <= r:
            m = (l + r) // 2
            left, mid, right = mountain_arr.get(m - 1), mountain_arr.get(m), mountain_arr.get(m + 1)

            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break

        peak = m

        # search left portion
        l, r = 0, peak
        while l <= r:
            mid = l + (r - l) // 2
            val = mountain_arr.get(mid)

            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return mid

        # search right portion
        l, r = peak, N - 1
        while l <= r:
            mid = l + (r - l) // 2
            val = mountain_arr.get(mid)

            if val > target:
                l = mid + 1
            elif val < target:
                r = mid - 1
            else:
                return mid
        
        return -1