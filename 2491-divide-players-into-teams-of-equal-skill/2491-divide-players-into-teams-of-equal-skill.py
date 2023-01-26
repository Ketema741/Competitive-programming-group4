class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        left, right = 0, len(skill) - 1
        skill.sort()
        chemistry = 0
        skill_sum = skill[0] + skill[-1]
        while left < right:
            if skill[left] + skill[right] != skill_sum:
                return -1
            else:
                chemistry += skill[left]*skill[right]
                left += 1
                right -= 1
        
        return chemistry