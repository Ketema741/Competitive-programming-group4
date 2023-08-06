class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        largest = max(candies)
        
        for candy in candies:
            if candy + extraCandies >= largest:
                res.append(True)
            else:
                res.append(False)
                
        return res