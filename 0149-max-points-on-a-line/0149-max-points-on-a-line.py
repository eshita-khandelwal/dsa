class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        #calculate the slope for any 2 points and keep a count
        res = 1
        for i in range(len(points)):
            count = collections.defaultdict(int)
            slope = 0
            for j in range(i+1,len(points)):
                if points[i][0] == points[j][0]:
                    slope = float("infinity")
                else:
                    slope = (points[j][1] - points[i][1])/(points[j][0] - points[i][0])
                count[slope]+=1
                res = max(res,count[slope]+1)
        return res
