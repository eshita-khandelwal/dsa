class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
     
        result.append(1)
        for i in range(1,n):
            result.append(result[i-1] * nums[i-1])
        print(result)
        postFix = 1
        for i in range(n-1,-1,-1):
            result[i]=result[i] * postFix
            postFix = postFix * nums[i]
        return result

            