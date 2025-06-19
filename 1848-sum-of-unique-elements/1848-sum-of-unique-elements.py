class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums.sort()
        sum1 = 0
        i = 0
        if len(nums) ==1:
            return nums[0]
        while i<len(nums):
            if i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=2
            elif i-1 > 0 and nums[i]== nums[i-1] : 
                i+=1
            else:
                if i == len(nums)-1:
                    if nums[i]== nums[i-1]:
                        return sum1
                    else:
                        sum1+=nums[i]
                        return sum1
                sum1+=nums[i]
                i+=1
        
        return sum1



