class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        monoStack = []
        second = -math.inf
        
        for num in nums[::-1]:
            if num < second:
                return True
            
            while monoStack and monoStack[-1] < num:
                second = monoStack.pop()
            

            monoStack.append(num)
            
        return False