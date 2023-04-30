class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent 
        self.locked = [None] * len(parent)
        self.child = {i:[] for i in range(len(parent))}
        
        for i in range(1, len(parent)):
            self.child[parent[i]].append(i)
        

    def lock(self, num: int, user: int) -> bool:
        if self.locked[num]:
            return False
        self.locked[num] = user
        return True
        

    def unlock(self, num: int, user: int) -> bool:
        if self.locked[num] != user:
            return False
        self.locked[num] = None
        return True

    def upgrade(self, num: int, user: int) -> bool:
        i = num
        while i != -1:
            if self.locked[i]:
                return False
            
            i = self.parent[i]
        
        locked_count = 0
        queue = deque([num])
        
        while queue:
            node = queue.popleft()
            if self.locked[node]:
                self.locked[node] = None
                locked_count += 1
            queue.extend(self.child[node])
            
        if locked_count > 0:
            self.locked[num] = user
            
        
        return locked_count > 0

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)