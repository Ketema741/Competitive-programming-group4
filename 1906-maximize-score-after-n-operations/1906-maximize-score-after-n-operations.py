class Solution:
    def maxScore(self, nums: List[int]) -> int:
        cache = defaultdict(int)

        def dfs(mask, opp):
            if mask in cache:
                return cache[mask]

            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if (1 << i) & mask or (1 << j) & mask:
                        continue
                    newMask = mask | (1 << i) | (1 << j)
                    score = opp * math.gcd(nums[i], nums[j])

                    cache[mask] = max(cache[mask], score + dfs(newMask, opp + 1))

            return cache[mask]

        return dfs(0, 1)