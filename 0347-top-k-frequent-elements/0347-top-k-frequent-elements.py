class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #use bucket sort here, this solution is o(n)
        res = []
        count = {} #get the freq of each number
        freq = [[] for i in range(len(nums)+1)] #stores freq->[]list of nums having that freq. 
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i],0)
        for key,val in count.items():
            freq[val].append(key)
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
        return res