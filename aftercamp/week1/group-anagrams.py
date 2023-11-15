class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        res = []

        for indx, s in enumerate(strs):
            sorted_word = ''.join(sorted(s))
            hash_map[sorted_word].append(s)
            
        return hash_map.values()

"""
    "eat","tea","tan","ate","nat","bat"

    count = [0, 0, 0, 0, 0, 0] 26
    a = 65
    b = 67
    {}
    hash_map[sort] = 
"""