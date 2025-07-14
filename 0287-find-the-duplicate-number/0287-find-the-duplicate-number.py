class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            a = abs(nums[i])
            if nums[a-1]<0:
                return abs(nums[i])
            nums[a-1] = -1 * nums[a-1]
        return -1
