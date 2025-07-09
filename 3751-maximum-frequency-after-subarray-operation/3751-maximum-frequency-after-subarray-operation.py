class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        kc = nums.count(k) #count all k in nums
        max1 = 0
        for i in range(51):
            mx = 0
            c= 0
            for j in nums:
                if j == k:
                    c-=1
                if j == i:
                    c+=1
                mx = max(mx,c)
                c = max(0,c)
            max1 = max(max1,mx)
        return kc + max1


