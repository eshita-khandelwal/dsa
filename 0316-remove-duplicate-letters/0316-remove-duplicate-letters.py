class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        seen = set()
        count = {}
        for i in range(len(s)):
            count[s[i]] = i
        for i in range(len(s)):
            if s[i] not in seen:
                while stack and s[i]<stack[-1] and i<count[stack[-1]]: #if the current character is smaller and the top character appears later in the string then we can pop it.
                    seen.discard(stack.pop())
                seen.add(s[i])
                stack.append(s[i])
        return "".join(stack)