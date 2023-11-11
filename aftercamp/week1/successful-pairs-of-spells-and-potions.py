class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        N = len(potions)
        res = []

        for num in spells:
            left, right = 0, N - 1

            while left <= right:
                mid = left + ( right - left)//2

                if num * potions[mid] >= success:
                    right = mid - 1
                else:
                    left = mid + 1

            res.append(N - left)
        
        return res
