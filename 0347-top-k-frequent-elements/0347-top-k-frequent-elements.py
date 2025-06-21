class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #time complexity is O(n)
        count = {} #hashmap to count frequency of each element
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = count.get(n,0) + 1
        
        for key,val in count.items():
            freq[val].append(key)
        
        res = []
        print(freq)
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                if len(res)==k:
                    return res
                res.append(n)
        return res
