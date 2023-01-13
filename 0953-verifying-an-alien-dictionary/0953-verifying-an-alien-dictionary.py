class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hash_map = defaultdict()
        for indx, val in enumerate(order):
            hash_map[val] = indx
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                if words[i][j] != words[i+1][j]:
                    if hash_map[words[i][j]] > hash_map[words[i+1][j]]:
                        return False
                    break
        return True
        