class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubseq(s, p):
            ptr1, ptr2 = 0, 0

            while ptr1 < len(s) and ptr2 < len(p):
                if ptr1 not in removed and s[ptr1] == p[ptr2]:
                    ptr2 += 1

                ptr1 += 1
            
            return ptr2 == len(p)

        left, right = 0, len(removable) - 1
        res = 0

        while left <= right:
            mid = left + (right - left)//2
            removed = set(removable[:mid + 1])

            if isSubseq(s, p):
                left = mid + 1
                res = max(res, mid + 1)
            else:
                right = mid - 1
        
        return res
