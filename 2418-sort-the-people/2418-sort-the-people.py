class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        for index in range(1, len(names)):            
            for j in range(index, 0, -1):
                if heights[j] > heights[j-1]:
                    names[j-1], names[j] = names[j], names[j-1]
                    heights[j-1], heights[j] = heights[j], heights[j-1]
                
        return names