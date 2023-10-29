class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack, res = [], []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
                
            if closedN < openN:
                stack.append(")")
                backtrack(openN, 1 + closedN)
                stack.pop()

        backtrack(0, 0)
        return res