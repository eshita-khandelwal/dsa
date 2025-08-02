class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if i-1 >=0 and nums[i] == nums[i-1]:
                continue
            t = -nums[i]
            l,r = i+1, len(nums)-1
            while l <r:
                # print(nums[i],nums[l],nums[r])
                if nums[l] + nums[r] == t:
                    res.append([nums[i],nums[l],nums[r]])
                    prev = nums[l]
                    while l <r and nums[l] == prev:
                        l+=1
                elif nums[l] + nums[r] > t:
                    r -=1
                else:
                    l +=1
                
        return res