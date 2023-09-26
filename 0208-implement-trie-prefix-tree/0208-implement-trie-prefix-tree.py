class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if cur.children[ord(c) - ord("a")] is None:
                cur.children[ord(c) - ord("a")] = TrieNode()
            cur = cur.children[ord(c) - ord("a")]
        cur.is_end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if cur.children[ord(c) - ord("a")] is None:
                return False
            cur = cur.children[ord(c) - ord("a")]
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if cur.children[ord(c) - ord("a")] is None:
                return False
            cur = cur.children[ord(c) - ord("a")]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)