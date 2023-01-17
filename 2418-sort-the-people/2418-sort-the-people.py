class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        max_ = max(heights[:])
        counter = [0] * (max_ + 1)
        res = []
        dict = {height: name for height, name in zip(heights, names)}
        for height in heights:
            counter[height] += 1
        
        for indx, count in enumerate(counter):
            if count:
                for i in range(count):
                    res.append(dict[indx])
                
                
        return res[::-1]