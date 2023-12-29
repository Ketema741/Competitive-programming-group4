class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        res = 0
        high, flipped = 0, 0

        for num in flips:
            flipped += 1

            if num > high:
                high = num

            if flipped == high:
                res += 1
        
        return res
            