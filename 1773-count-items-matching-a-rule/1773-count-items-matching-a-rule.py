class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        hash_map = {'type': 0, 'color': 1, 'name': 2}
        res = 0
        
        for item in items:
            if item[hash_map[ruleKey]] == ruleValue:
                res += 1
        
        return res