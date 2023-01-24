class Solution(object):
    def largestNumber(self, nums):
        def func(n1, n2):
            return 1 if n1+n2<n2+n1 else -1
        
        ans = sorted([str(n) for n in nums], key=cmp_to_key(func))
        
        if ans[0] == '0':
            return '0'
        else:
            return ''.join(ans)