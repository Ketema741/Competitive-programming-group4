class Solution(object):
    def findOriginalArray(self, changed):
        changed.sort()
        queue, res = deque(), []

        if len(changed)  % 2 != 0:
            return []

        for num in changed:
            if queue and queue[0]*2 == num:
                res.append(queue.popleft())
            else:
                queue.append(num)

        return res if not queue else []
"""
    1 3 4 2 6 8
    1 2 3 4 6 8 
    
    Sort original array 
    Iterate the array, First find doubled value for smaller number which is
    the one at the beginning 
    then append smaller nums to deque double it and compare it current value
    if they are equal popleft and add to answer 
    COMPLEXITY
    Time: O(nlogn) Sorting
    Space: O(n) stack
   
"""
        