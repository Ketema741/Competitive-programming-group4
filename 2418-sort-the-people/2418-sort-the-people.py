class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        for index, name in enumerate(names):
            for j in range(1, len(names) - index):
                if heights[j-1] < heights[j]:
                    names[j-1], names[j] = names[j], names[j-1]
                    heights[j-1], heights[j] = heights[j], heights[j-1]
        return names