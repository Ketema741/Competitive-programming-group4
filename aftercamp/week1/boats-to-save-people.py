class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left, right = 0, len(people) - 1
        people.sort(reverse=True)
        count = 0
        
        while left <= right :
            if people[left] > limit:
                count += 1
                left += 1
            elif people[left] + people[right] <= limit:
                count += 1
                right -= 1
                left += 1 
            else:
                count += 1
                left += 1
                
        return count