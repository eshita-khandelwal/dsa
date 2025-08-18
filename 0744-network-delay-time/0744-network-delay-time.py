class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for n1,n2,w1 in times:
            adj[n1].append((w1,n2))
        
        minHeap = []
        minHeap.append((0,k))
        heapq.heapify(minHeap)
        visit = set()
        max1 = -1
        while minHeap:
            w1,n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            max1 = max(max1,w1)
            for w2,nei in adj[n1]:
                if nei not in visit:
                    heapq.heappush(minHeap,(w1+w2,nei))
        
        return max1 if len(visit)==n else -1
            
