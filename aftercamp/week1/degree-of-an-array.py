class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first_occurrence = {}
        last_occurrence = {}
        frequency = {}
        
        max_degree = 0
        min_length = 0

        for i, num in enumerate(nums):
            if num not in first_occurrence:
                first_occurrence[num] = i
            last_occurrence[num] = i
            frequency[num] = frequency.get(num, 0) + 1
            
            if frequency[num] > max_degree:
                max_degree = frequency[num]
                min_length = last_occurrence[num] - first_occurrence[num] + 1
            elif frequency[num] == max_degree:
                min_length = min(min_length, last_occurrence[num] - first_occurrence[num] + 1)
        
        return min_length