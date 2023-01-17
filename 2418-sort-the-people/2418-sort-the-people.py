class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        for index in range(len(names)):
            max_index = index
            
            for j in range(index + 1, len(names) ):
                if heights[max_index] < heights[j]:
                    max_index = j
                    
            if max_index != index:
                names[max_index], names[index] = names[index], names[max_index]
                heights[max_index], heights[index] = heights[index], heights[max_index]
                
        return names