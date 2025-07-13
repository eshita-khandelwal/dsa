class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals = sorted(intervals)
        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if res[len(res)-1][1] >= intervals[i][0]:
                interval = res.pop()
                interval[1] = max(intervals[i][1],interval[1])
                res.append(interval)
            else:
                res.append(intervals[i])
        return res