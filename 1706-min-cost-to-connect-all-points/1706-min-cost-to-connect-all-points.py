class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #we will use minimum spanning trees algorithm and we will use prim's algo for that
        adj = collections.defaultdict(list)
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                dist = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        minHeap = []
        heapq.heappush(minHeap,[0,0])
        visit = set()
        res = 0
        while len(visit)<len(points):
            cost,v = heapq.heappop(minHeap)
            if v in visit:
                continue
            res +=cost
            visit.add(v)
            for neiC, nei in adj[v]:
                if nei not in visit:
                    heapq.heappush(minHeap,[neiC,nei])
        return res
