class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash_map = defaultdict(int)

        for val in arr:
            hash_map[val] += 1
        
        occurrences = list(hash_map.values())
        print(occurrences)

        return len(set(occurrences)) == len(occurrences)