class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        countZero = 0
        countOne = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                countZero+=1
            if nums[r] == 1:
                countOne +=1
            while countZero > k:
                if nums[l] == 0:
                    countZero -=1
                if nums[l] == 1:
                    countOne -=1
                l+=1
            res = max(res,r-l+1)
        return res
