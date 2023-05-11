class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0] * N
        nums = list(enumerate(nums))
        
        def merge(start, mid, end):
            
            p1, p2 = start, mid + 1
            
            temp = []
            count = 0
            
            while p1 <= mid and p2 <= end:
                if nums[p1][1] <= nums[p2][1]:
                    temp.append(nums[p1])
                    res[nums[p1][0]] += count
                    p1 += 1
                else:
                    temp.append(nums[p2])
                    count += 1
                    p2 += 1
                    
                    
            while p1 <= mid:
                temp.append(nums[p1])
                res[nums[p1][0]] += count
                p1 += 1
                
            while p2 <= end:
                temp.append(nums[p2])
                p2 += 1
                
            nums[start:end+1] = temp
            
        def mergeSort(start, end):
            if start >= end:
                return 
            
            mid = start + (end - start) // 2
            
            mergeSort(start, mid)
            mergeSort(mid+1, end)
            merge(start, mid, end)
    
        mergeSort(0, N - 1)
        
        return res
