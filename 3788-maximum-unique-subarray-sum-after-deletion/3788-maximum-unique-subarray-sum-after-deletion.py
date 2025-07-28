class Solution:
    def maxSum(self, nums: List[int]) -> int:
        res = -101
        s = 0
        l = 0
        count = collections.defaultdict(int)
        for i in range(len(nums)):
            if count[nums[i]] > 0:
                s -=nums[i]
                count[nums[i]] -=1
            if nums[i] > 0:
                s +=nums[i]
                count[nums[i]] = 1
                res = max(res,s)
        return res if res!=-101 else max(nums)


                
