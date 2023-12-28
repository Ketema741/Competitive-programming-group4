from collections import defaultdict

def count_pairs(nums, k):
    res = 0
    m = defaultdict(list)
    
    # Storing indices of numbers in a defaultdict
    for i, num in enumerate(nums):
        m[num].append(i)
    
    for n, ids in m.items():
        gcds = defaultdict(int)
        for i in ids:
            gcd_i = gcd(i, k)  # Assuming gcd function is defined
            for gcd_j, cnt in gcds.items():
                res += gcd_i * gcd_j % k == 0  # Check if the condition is met
            gcds[gcd_i] += 1
    
    return res
    
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        res = 0
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and i*j % k == 0:
                    res += 1
        return res
                    