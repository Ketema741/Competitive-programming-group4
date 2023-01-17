class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        N = len(arr)
        max_ = -1
        for index in range(N - 1 , -1, -1):
            temp =  arr[index]
            arr[index] = max_
            max_ = max(max_, temp)
            
           
        return arr