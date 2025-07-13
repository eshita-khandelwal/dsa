class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findleft(nums,target):
            l,r = 0,len(nums)-1
            left = -1
            while l<=r:
                m = (l+r)//2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    left = m
                    r = m-1
            return left
            
        def findright(nums,target):
            l,r = 0,len(nums)-1
            right = -1
            while l<=r:
                m = (l+r)//2
                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    right = m
                    l = m + 1
            return right

        leftmost = findleft(nums,target)
        if leftmost == -1:
            return [-1,-1]
        rightmost = findright(nums,target)
        return [leftmost,rightmost]
