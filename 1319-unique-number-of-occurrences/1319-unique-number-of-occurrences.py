class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for i in range(len(arr)):
            count[arr[i]] = 1 + count.get(arr[i],0)
        seen = set()
        for key,val in count.items():
            if val in seen:
                return False
            seen.add(val)
        return True



            
