class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}  # num -> frequency
        freq = [[] for i in range(len(nums)+1)]  # index = frequency, value = list of numbers

        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)  # count frequencies

        for key, val in count.items():
            freq[val].append(key)  # bucket sort based on frequency

        for i in range(len(freq)-1, -1, -1):  # go from highest freq to lowest
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        return res
