from cmath import inf
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.val = 0
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, binary):
        cur = self.root
        for char in binary:
            cur = cur.children[int(char)]
    
    def maxXOR(self, binary) -> int:
        result = 0
        cur = self.root
        for  char in binary:
            opposite = 1 - int(char)
            if opposite in cur.children:
                result = (result << 1) | 1
                cur = cur.children[opposite]
            else:
                result = (result << 1)
                cur = cur.children[int(char)]
        return result

def findMaximumXOR(nums):
    trie = Trie()
    result = -inf
    maxLen = len(bin(max(nums))[2:])
    
    for num in nums:
        key = bin(num)[2:].zfill(maxLen)
        trie.insert(key)
        result = max(result, trie.maxXOR(key))
        
    return result

input_len = int(input())
for _ in range(input_len):
    n = int(input())
    nums = list(map(int, input().split()))

    print(findMaximumXOR(nums))