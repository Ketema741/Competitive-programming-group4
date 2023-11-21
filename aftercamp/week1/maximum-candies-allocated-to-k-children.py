class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(mid):
            count = 0
            for candy in candies:
                count += floor(candy/mid)
            
            return count >= k

        left, right = 1, max(candies)

        while left <= right:
            mid = (left + right)//2

            if check(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right
