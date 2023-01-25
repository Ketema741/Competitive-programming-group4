class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash_map = defaultdict()
        res = []
        for indx, char in enumerate(s):
            hash_map[char] = indx

        max_ = hash_map[s[0]]
        end = 0
        print(hash_map)
        for indx, char in enumerate(s):
            if hash_map[char] > max_:
                max_ = hash_map[char]
            if max_ == indx:
                max_ += 1
                res.append(max_ - end)
                end = max_
        return res