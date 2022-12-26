class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {}
        losers = {}
        
        for match in matches:
            winners[match[0]] = 1 + winners.get(match[0], 0)
            losers[match[1]] = 1 + losers.get(match[1], 0)
            
        winners_list = list(set(winners.keys()) - set(losers.keys()))
        losers_list = []
        
        for key, value in losers.items():
            if value == 1:
                losers_list.append(key)
        losers_list.sort()
        winners_list.sort()
        return [winners_list, losers_list]