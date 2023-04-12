"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        visited = set()
        graph = defaultdict(list)        
        for employee in employees:
            id_, impo, sub = employee.id, employee.importance, employee.subordinates
            graph[id_].append(impo)
            graph[id_].append(sub)
        
        
        def dfs(id):
            target = graph[id]
            res = target[0]
            visited.add(id)

            for sub_id in target[1]:
                if sub_id not in visited:
                    res += dfs(sub_id)

            return res

        return dfs(id)