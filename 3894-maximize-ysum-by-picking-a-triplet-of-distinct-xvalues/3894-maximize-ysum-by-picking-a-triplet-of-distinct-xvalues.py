class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        res = 0
        xres = {}
        yval = []
        for i in range(len(y)):
            yval.append([-y[i],i])
        heapq.heapify(yval)
        #print(yval)
        while yval:
            if len(xres) == 3:
                break
            val,idx = heapq.heappop(yval)
            if x[idx] not in xres:
                xres[x[idx]] = idx

        for key,val in xres.items():
            res+=y[val]
        return res if len(xres)==3 else -1
