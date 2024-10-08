class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        #dp[len(word1)][len(word2)]=1
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j]=1+dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        
        if dp[0][0]==len(word1):
            return len(word2)-dp[0][0]
        if dp[0][0]==len(word2):
            return len(word1)-dp[0][0]
        return len(word2)-dp[0][0] + len(word1)-dp[0][0]
        
                