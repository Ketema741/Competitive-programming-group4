from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.count = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.children[char]
            
        curr.count += 1
        
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        curr = self.root
        count = 0
        
        for word in words:
            self.addWord(word)
        
        def dfs(i, root):
            nonlocal count
            if not root:
                return 
            
            count += root.count
            
            for char in root.children:
                for j in range(i, len(s)):
                    if s[j] == char:
                        dfs(j + 1, root.children[char])
                        break
        dfs(0, curr)
        
        return count