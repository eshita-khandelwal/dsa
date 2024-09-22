class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        l=0
        r=0
        count = {}
        maxf,maxn=0,0
        count2 = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i],0)
            if nums[i] not in count2:
                count2[nums[i]]=[]
                count2[nums[i]].append(i)
            else:
                count2[nums[i]].append(i)
            if maxf<count[nums[i]]:
                maxf=count[nums[i]]
        
        min1 = float("inf")
        for [key,val] in count.items():
            if val==maxf:
                min1 = min(min1,count2[key][len(count2[key])-1]-count2[key][0]+1)
        
        return min1
        