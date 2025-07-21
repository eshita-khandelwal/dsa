class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        #time complexity is O(mn)
        n,m = len(rooms), len(rooms[0])
        q = deque()
        visit = set()
        def addToQ(r,c):
            if r<0 or r==n or c<0 or c==m or (r,c) in visit or rooms[r][c] == -1:
                return
            q.append([r,c])
            #visit.add((r,c))

        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    q.append([i,j])
                    #visit.add((i,j))
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                rooms[r][c] = min(dist,rooms[r][c])
                visit.add((r,c))
                addToQ(r+1,c)
                addToQ(r-1,c)
                addToQ(r,c-1)
                addToQ(r,c+1)
            dist+=1
        

