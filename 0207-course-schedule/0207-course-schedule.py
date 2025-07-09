class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #indegree is important here ? - finds cycles
        q = deque()
        graph = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses

        for i in range(len(prerequisites)):
            graph[prerequisites[i][1]].append(prerequisites[i][0])
            indegree[prerequisites[i][0]] +=1
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        nodesVisited = 0

        while q:
            cur = q.popleft()
            nodesVisited +=1
            for nei in graph[cur]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return nodesVisited == numCourses
