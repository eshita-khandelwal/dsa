class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)} 
        indegree = [0] * numCourses
        q = deque()
        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a] +=1
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        nodesVisited = 0
        while q:
            course = q.popleft()
            nodesVisited +=1
            for neiCourse in adj[course]:
                indegree[neiCourse]-=1
                if indegree[neiCourse] == 0:
                    q.append(neiCourse)
        
        return nodesVisited == numCourses


        
