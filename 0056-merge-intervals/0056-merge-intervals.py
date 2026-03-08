class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        res = [[start,end]]
        for i in range(1,len(intervals)):
            if res[len(res)-1][1] >= intervals[i][0]:
                start,end = res.pop()
                res.append([start,max(intervals[i][1],end)])
            else:
                res.append(intervals[i])
        return res   
