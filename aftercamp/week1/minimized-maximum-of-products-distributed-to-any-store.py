class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def check(mid):
            count = 0
            for val in quantities:
                count += ceil(val/mid)

            return count <= n

        left, right = 1, max(quantities)

        while left <= right:
            mid = (left + right)//2

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

