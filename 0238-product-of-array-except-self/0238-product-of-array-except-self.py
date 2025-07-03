class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref, suff = [1], [1]
        for i in range(1,len(nums)):
            pref.append(pref[len(pref)-1] * nums[i-1])
        n = len(nums)
        for i in range(n-2,-1,-1):
            suff.append(nums[i+1] * suff[len(suff)-1])
        res = []
        print(pref)
        print(suff)
        for i in range(n):
            res.append(pref[i] * suff[n-i-1])
        
        return res


