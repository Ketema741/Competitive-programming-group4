class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        res = 0
        
        for i in range(R - 2):
            for j in range(C - 2):
                sum_ = 0
                # top horizontal items
                for k in range(j, j + 3):
                    
                    sum_ += grid[i][k]

                # middle items
                sum_ += grid[i + 1][j + 1]
                
                 # bottom horizontal items
                for k in range(j, j + 3):
                   sum_ += grid[i + 2][k]
                res = max(res, sum_)
        return res

    """
        class Solution:
            def maxSum(self, x: List[List[int]]) -> int:

                # initialize max to 0
                mx = 0

                m = len(x) = 4
                n = len(x[0]) = 4

                # traverse through 
                # rows: m-3 times
                # columns: n-3 times for each row
                1  2  3
                   4  
                7  8  9
                for i in range(2):
                    for j in range(2):

                        # add top horizontal items
                        mSum = 0
                        for k in range(j, j+3):
                            mSum += x[i][k]

                        # add bottom horizontal items
                        for k in range(j, j+3):
                            mSum += x[i+2][k]

                        # add middle element of the hourglass
                        mSum += x[i+1][j+1]

                        # update max if we get new maximum
                        if mx < mSum:
                            mx = mSum
                return mx
                mSum = 
    """