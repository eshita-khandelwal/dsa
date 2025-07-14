class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dp = {} #caching
        wordsset = set(words)
        res = []
        def dfs(word):
            if word in dp:
                return dp[word]
            
            for i in range(1,len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if (prefix in wordsset and suffix in wordsset) or (prefix in wordsset and dfs(suffix)):
                    dp[word] = True
                    return True
            dp[word] = False
            return False
        for word in words:
            if dfs(word):
                res.append(word)
        return res

