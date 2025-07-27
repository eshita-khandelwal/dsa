class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        #stop - > stop relation will give us TLE so we will build stop->route relationship in adj matrix. we will add all the stops for the current stop's route to the queue
        adj = collections.defaultdict(set)
        for i in range(len(routes)):
            for stop in routes[i]:
                adj[stop].add(i)
        
        q = deque() #we will add the stops in this queue
        visit = set()
        bus = 0
        q.append(source)
        visit.add(source)
        visited_routes = [False] * len(routes)
        while q:
            for i in range(len(q)):
                stop = q.popleft()
                if stop == target:
                    return bus
                for routeId in adj[stop]:
                    if not visited_routes[routeId]:
                        visited_routes[routeId] = True
                        for x in routes[routeId]:
                            if x not in visit:
                                q.append(x)
                                visit.add(x)
            bus +=1
        return -1