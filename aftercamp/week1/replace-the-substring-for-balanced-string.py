class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        hash_map = defaultdict(int)

        for char in s:
            hash_map[char] += 1
            
        if self.isBalanced(hash_map, n//4):
            return 0

        res = float("inf")
        left = right = 0

        while right < n:
            hash_map[s[right]] -= 1

            while self.isBalanced(hash_map, n//4) and left <= right:
                res = min(res, right - left +1)
                hash_map[s[left]] += 1
                left += 1
            
            right += 1

        return res


        
    def isBalanced(self, hash_map, n):
            return max(hash_map.values()) == n
                
                
"""
n = 2
 0  1  2  3  4  5  6  7
 Q  R  R  R  W  E  R  E
l                 ^
r                  ^
n = 8
each = 2
Q: 1
R: 2
W: 1
E: 2

"""