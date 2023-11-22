class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res =  [[1]]
        
        for _ in range(numRows - 1):
            temp = [1]

            for i in range(1, len(res[-1])):
                temp.append(res[-1][i - 1] + res[-1][i])

            temp.append(1)
            res.append(temp)

        return res