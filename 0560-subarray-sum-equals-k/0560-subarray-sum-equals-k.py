class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #hashmap is total:freq
        #{0:1} # we put this becasue is will never be calculated
        hashMap = {0:1}
        total = count = 0
        for i in range(len(nums)):
            total+=nums[i]
            if total-k in hashMap:
                count+=hashMap[total-k]
            
            hashMap[total] = 1 + hashMap.get(total,0)
        
        return count
            
