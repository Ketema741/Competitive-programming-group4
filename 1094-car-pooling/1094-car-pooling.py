class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        lastDrop = -1
        
        for trip in trips:
            lastDrop = max(lastDrop, trip[-1])
        events = [0]*(lastDrop + 1)
        
        for passengers, start, end in trips:
            events[start] += passengers
            events[end] -= passengers
        
        if events[0] > capacity:
            return False
        
        for i in range(1, len(events)):
            events[i] += events[i-1]
            if events[i] > capacity:
                return False
            
        return True