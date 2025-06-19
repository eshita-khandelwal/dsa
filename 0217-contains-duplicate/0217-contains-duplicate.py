class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}

        for n in nums:
            if n in hash_map:
                return True
            else:
                hash_map[n] = hash_map.get(n,1) + 1
        
        return False