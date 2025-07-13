class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c=='{' or c =='[':
                stack.append(c)
            else:
                if stack:
                    x = stack.pop()
                    if c == ')' and x!='(':
                        return False
                    elif c == '}' and x!='{':
                        return False
                    elif c == ']' and x!='[':
                        return False
                else:
                    return False
        return True if len(stack) == 0 else False
                    
