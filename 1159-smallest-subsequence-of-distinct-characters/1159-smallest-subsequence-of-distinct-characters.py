class Solution:
    def smallestSubsequence(self, s: str) -> str:
        count = {}
        stack = []
        seen = set()
        for i in range(len(s)):
            count[s[i]]=i
        for i in range(len(s)):
            if s[i] not in seen:
                while stack and s[i]<stack[-1] and i<count[stack[-1]]:
                    seen.discard(stack[-1])
                    stack.pop()
                stack.append(s[i])
                seen.add(s[i])
        return "".join(stack)
                    