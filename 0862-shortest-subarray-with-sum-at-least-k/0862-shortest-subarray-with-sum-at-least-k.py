class Solution(object):
    def shortestSubarray(self, nums, K):
        N, prefix_sum = len(nums), [0]
        
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        # Want smallest right - left with Pr - Pl >= K
        ans = N + 1 # N+1 is impossible
        monoq = collections.deque() # opt(right) candidates, represented as indices of prefix_sum
        
        for right, Pr in enumerate(prefix_sum):
            
            # Want opt(r) = largest l with Pl <= Pr - K
            while monoq and Pr <= prefix_sum[monoq[-1]]:
                monoq.pop()

            while monoq and Pr - prefix_sum[monoq[0]] >= K:
                ans = min(ans, right - monoq.popleft())

            monoq.append(right)

        return ans if ans < N + 1 else -1  