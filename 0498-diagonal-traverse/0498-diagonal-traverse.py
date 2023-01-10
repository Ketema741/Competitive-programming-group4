class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        hash_map = defaultdict(list)
        res = []
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                hash_map[row + col].append(mat[row][col])
        print(hash_map)
        for key, val in hash_map.items():
            if key%2 == 0:
                res.extend(val[::-1])
            else:
                
                res.extend(val)
        return res
            
        
        