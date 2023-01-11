class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [indx for indx in range(1, n+1)]
        i = 0
        while len(arr) > 1:
            n = len(arr)
            i = (i + k-1) % n
            arr.pop(i)
        return arr[0]
            
        