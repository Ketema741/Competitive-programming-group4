class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        hash_map = defaultdict(list)
        count = 0
        for col_idx in range(len(strs[0])):
             for row_idx in range(len(strs)):
                    hash_map[col_idx]. append(strs[row_idx][col_idx])
        for strings in hash_map.values():
            if strings != sorted(strings):
                count += 1
        return count