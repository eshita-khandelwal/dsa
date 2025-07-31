class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #use bottom up approch and time complexity is o(amount * len(coins))
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for a in range(1,amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a] = min(dp[a],dp[a-c]+1)
        return dp[amount] if dp[amount]!=amount+1 else -1