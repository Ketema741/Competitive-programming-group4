class TrieNode:
    def __init__(self):
        self.children = {}
        self.score = 0
    
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        node = self.root
        delta = val - self.map.get(key, 0)
        
        self.map[key] = val
        
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
                
            node = node.children[char]
            node.score += delta
            

    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
            
        return node.score
        

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)