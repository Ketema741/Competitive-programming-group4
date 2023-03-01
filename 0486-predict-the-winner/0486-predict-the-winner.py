class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def turn(l, r, player):
            if l > r: return 0
            
            if player: 
                return max(nums[l]+ turn(l + 1, r, not player), nums [r] + turn(l, r-1, not player)) 
            else: 
                return min(-nums[l]+ turn(l + 1, r, not player), -nums[r] + turn(l, r-1, not player))
            
        return turn(0, len(nums) -1, True) >= 0