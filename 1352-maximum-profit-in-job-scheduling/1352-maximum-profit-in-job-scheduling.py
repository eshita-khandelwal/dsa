class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        #use brute force approch + caching 
        #we either choose a job or we don't choose a job
        intervals = sorted(zip(startTime,endTime,profit))
        cache = {}
        def binary_search(val):
            l = 0
            r = len(intervals)-1
            while l<=r:
                m = (l+r) //2 
                s,e,p = intervals[m]
                if s<val:
                    l = m+1
                else:
                    r = m-1
            return l
               


        def dfs(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]
            #don't select i job for profit
            res1 = dfs(i+1)
            #select
            j = binary_search(intervals[i][1])
            res2 = intervals[i][2]+dfs(j)
            cache[i] = max(res1,res2)
            return cache[i]
        return dfs(0)

