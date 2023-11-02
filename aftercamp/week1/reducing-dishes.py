class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)

        max_coef = 0
        current_coef = 0
        total_sat = 0

        for s in satisfaction:
            total_sat += s
            current_coef += total_sat
            max_coef = max(max_coef, current_coef)

        return max_coef
        