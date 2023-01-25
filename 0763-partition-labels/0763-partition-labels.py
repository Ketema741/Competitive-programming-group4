class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_map = defaultdict()
        res = []
        
        for indx, char in enumerate(s):
            hash_map[char] = indx

        left, max_len = 0, hash_map[s[0]]

        for right, char in enumerate(s):
            if hash_map[char] > max_len:
                max_len = hash_map[char]
                
            if max_len == right:
                max_len += 1
                res.append(max_len - left)
                left = max_len
                
        return res