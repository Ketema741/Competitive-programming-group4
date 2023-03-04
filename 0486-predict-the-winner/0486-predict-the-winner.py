class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def turn(l, r, player):
            if l > r: return 0
            
            if player: 
                score1 = nums[l] + turn(l + 1, r, not player)
                score2 = nums[r] + turn(l, r - 1, not player)
                
                return max(score1, score2) 
            else: 
                score1 = -nums[l] + turn(l + 1, r, not player)
                score2 = -nums[r] + turn(l, r - 1, not player)
                
                return min(score1, score2)
           
        return turn(0, len(nums) -1, True) >= 0