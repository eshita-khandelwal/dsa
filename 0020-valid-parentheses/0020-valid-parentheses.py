class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = []
        i = 0
        while i<len(s):
            if s[i]=='(' or s[i] == '{' or s[i]=='[':
                stack1.append(s[i])
            else:
                if len(stack1)==0:
                    return False
                if s[i]==')' and stack1[len(stack1)-1]=='(':
                    stack1.pop()
                        
                elif s[i]=='}' and stack1[len(stack1)-1]=='{':
                    stack1.pop()
                    
                elif s[i]==']' and stack1[len(stack1)-1]=='[':
                    stack1.pop()
                else:
                    return False
            i+=1
        return True if len(stack1)==0 else False



