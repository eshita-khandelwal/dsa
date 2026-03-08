class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = set(nums)
        def generate(n,ans):
            if ans in res:
                return
            if n==len(nums):
                res.add(ans)
                return 
            ans+="0"
            generate(n+1,ans)
            ans = ans[:-1]
            ans+="1"
            generate(n+1,ans)
        generate(0,"")
        
        for x in res:
            if x not in nums:
                return x
        return ""
            
