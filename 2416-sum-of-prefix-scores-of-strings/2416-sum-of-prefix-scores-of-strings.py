class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        res = []
        def insert(word):
            node = root

            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                
                node = node.children[char]
                node.count += 1
                
        def sumPrefix(word):
            curr = root
            curPrefix = 0
            
            for char in word:
                curr = curr.children[char]
                curPrefix += curr.count
                
            return curPrefix
                
        for word in words:
            insert(word)
            
        for word in words:
            res.append(sumPrefix(word))
            
        return res