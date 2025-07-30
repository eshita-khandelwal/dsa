class Solution:
    def minNumberOfPrimes(self, n: int, m: int) -> int:
        dp = [n+1] * (n+1)
        dp[0] = 0
        k = m
        #get all the primes 
        coins = []
        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            return True
        
        for c in range(2,n+1):
            if k==0:
                break
            if is_prime(c):
                coins.append(c)
                k -=1
       
        for a in range(1,n+1):
            for c in coins:
                if a-c >=0:
                    dp[a] = min(dp[a],1+dp[a-c])
        return dp[n] if dp[n]!=n+1 else -1
