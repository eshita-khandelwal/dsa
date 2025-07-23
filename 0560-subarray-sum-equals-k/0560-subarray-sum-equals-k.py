class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currSum = 0
        count = {0:1}
        for n in nums:
            currSum +=n
            diff = currSum - k
            res += count.get(diff,0)
            count[currSum] = 1 + count.get(currSum,0)
        return res

# [1,1,1] -> currsum = 1, diff = 1-2 = -1, count= {0:1,1:1}
# currsum = 2 diff = 0 res = 1 count = {0:1,1:1,2:1}
# currsum 3 diff = 1 count = {0:1,1:1,2:1,3:1}