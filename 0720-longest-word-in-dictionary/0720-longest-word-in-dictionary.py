class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

class Solution:
    def longestWord(self, words):
        trie = Trie()

        for word in words:
            trie.insert(word)

        res = ""
        for word in words:
            curr = trie.root

            if len(word) < len(res) or (len(word) == len(res) and word > res):
                continue

            valid_word = True
            for char in word:
                curr = curr.children[char]
                if not curr.end_of_word:
                    valid_word = False
                    break

            if valid_word:
                res = word

        return res
