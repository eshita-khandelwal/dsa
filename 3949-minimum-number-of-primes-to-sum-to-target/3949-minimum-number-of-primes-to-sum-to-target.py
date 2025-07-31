class Solution:
    def minNumberOfPrimes(self, n: int, m: int) -> int:
        #same as coin change dp problem lets build the prime array first
        k = m
        coins = []
        def isPrime(i):
            for j in range(2,int(i**0.5)+1):
                if i%j == 0:
                    return False
            return True
        for i in range(2,n+1):
            if isPrime(i):
                coins.append(i)
            if len(coins) == m:
                break
        dp = [n+1] * (n+1)
        dp[0] = 0
        
        for a in range(1,n+1):
            for c in coins:
                if a-c>=0:
                    dp[a] = min(dp[a],1+dp[a-c])
        return dp[n] if dp[n]!=n+1 else -1
