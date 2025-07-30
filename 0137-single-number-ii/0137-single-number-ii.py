class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0,len(nums),3):
            if i+1<len(nums) and i+2 < len(nums) and nums[i] == nums[i+1] == nums[i+2]:
                continue
            else:
                return nums[i]