class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if target == nums[m]:
                return m
            #left sorted portion
            if nums[m] >= nums[l]:
                if nums[l] > target or nums[m] < target:
                    l = m+1
                else:
                    r = m - 1
            #right sorted portion
            else:
                if nums[r] < target or nums[m] > target:
                    r = m-1
                else:
                    l = m+1
            
        return -1 


