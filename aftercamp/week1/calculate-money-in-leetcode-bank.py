class Solution:
    def totalMoney(self, n: int) -> int:
        res, stack = 0, []

        round = 1

        for _ in range(n):

            if len(stack) == 7:
                round += 1
                res += sum(stack)
                stack = []

            if not stack:
                stack.append(round)
            else:
                stack.append(stack[-1] + 1)

        res += sum(stack)
        
        return res
        



