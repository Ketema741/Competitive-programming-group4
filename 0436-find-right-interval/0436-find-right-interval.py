class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        res = [-1]*n
        
        intervals = sorted([[start, end, indx] for indx, [start, end] in enumerate(intervals)])
        starts = [start for start,_,_ in intervals]
        
        for start, end, indx in intervals:
            
            start_indx = bisect.bisect_left(starts, end)
            
            if start_indx < n:
                res[indx] = intervals[start_indx][2]
                
        return res
    
