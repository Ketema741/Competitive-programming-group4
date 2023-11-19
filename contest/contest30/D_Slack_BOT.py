n = int(input())
words = []
for _ in range(n):
    word = input()
    words.append(word)

class TrieNode:
    def __init__(self):
        self.count = 0
        self.children = {}  

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]
            current.count += 1

    def findCommonPrefix(self, word: str) -> int:
        current = self.root
        common_prefix = 0

        for char in word:
            current = current.children.get(char)

            if current and current.count >= 2:
                common_prefix += 1
            else:
                break

        return common_prefix

ob = Trie()

for word in words:
    ob.insert(word)

for word in words:
    res = ob.findCommonPrefix(word)
    print(res)
