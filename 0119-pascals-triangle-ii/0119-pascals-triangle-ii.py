class Solution:
    def constructTriangle(self, rowIndex, nums):
        res = [1]
        if rowIndex == 0:
            return nums
        
        for i in range(1, len(nums)):
            res.append(nums[i-1] + nums[i])
            
        res.append(1)
        
        return self.constructTriangle(rowIndex - 1, res)
            
    def getRow(self, rowIndex: int) -> List[int]:
        res = self.constructTriangle(rowIndex, [1])
        return res