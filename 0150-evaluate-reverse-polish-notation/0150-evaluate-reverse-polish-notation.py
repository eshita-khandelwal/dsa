class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+": operator.add , "-": operator.sub , "*": operator.mul, "/": operator.truediv}
        for i in range(len(tokens)):
            if tokens[i].isdigit() or tokens[i].lstrip('-').isdigit():
                stack.append(tokens[i])
            else:
                if stack:
                    num1 = stack.pop()
                    if stack:
                        num2 = stack.pop()
                    res = operators[tokens[i]](float(num2), float(num1))
                    stack.append(str(int(float(res))))
        res = int(float(stack.pop()))
        return res
