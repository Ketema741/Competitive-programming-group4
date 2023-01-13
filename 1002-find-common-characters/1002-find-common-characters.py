class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res, hash_map = [],   defaultdict(list)    
        N, min_occurence = len(words), 0
        
        for index, word in enumerate(words):
            for char in word:
                hash_map[char].append(index)
                
        for key, value in hash_map.items():
            if len(set(value)) == N:
                min_occurence = min(Counter(value).values())
                for _ in range(min_occurence):
                    res.append(key)
        return res