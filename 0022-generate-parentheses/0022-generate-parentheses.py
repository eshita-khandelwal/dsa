class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #open < n , closed<open, open==closed==n : add to the result
        result = []
        stack = [] #used to add and pop, it is a global variable
        def backtrack(openN,closedN):
            if closedN == openN==n:
                result.append("".join(stack))
                return
            if openN<n:
                stack.append("(")
                backtrack(openN+1,closedN)
                stack.pop()
            if closedN<openN:
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop()
        backtrack(0,0)
        return result