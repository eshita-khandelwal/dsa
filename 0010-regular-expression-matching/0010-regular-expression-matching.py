# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         #top-down memoization
#         cache = {}
#         def dfs(i,j):
#             if i>=len(s) and j>=len(p):
#                 return True
#             if j>=len(p):
#                 return False #no more characters to compare with string s so False
#             match = i<len(s) and (s[i]==p[j] or p[j]=='.')
#             if j+1 < len(p) and p[j+1]=='*':
#                 cache[(i,j)] = dfs(i,j+2) or (match and dfs(i+1,j))
#                 return cache[(i,j)]
#             if match:
#                 cache[(i,j)] = dfs(i+1,j+1)
#                 return cache[(i,j)]
#             cache[(i,j)] = False
#             return False
#         return dfs(0,0)


class Solution(object):
    def isMatch(self, text: str, pattern: str) -> bool:
        memo = {}

        def dp(i: int, j: int) -> bool:
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], "."}
                    if j + 1 < len(pattern) and pattern[j + 1] == "*":
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

