class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def longestCommonPrefix(self):
        prefix = []
        node = self.root
        while node and not node.is_end_of_word and len(node.children) == 1:
            char = list(node.children.keys())[0]
            prefix.append(char)
            node = node.children[char]
        return "".join(prefix)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        trie = Trie()

        for word in strs:
            trie.insert(word)

        return trie.longestCommonPrefix()
