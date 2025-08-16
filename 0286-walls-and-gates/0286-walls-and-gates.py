class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        n,m = len(rooms),len(rooms[0])
        q = deque()
        seen = set()
        for i in range(n):
            for j in range(m):
                if rooms[i][j]==0:
                    q.append((i,j,0))
                    seen.add((i,j))
        
        
        while q:
            for i in range(len(q)):
                r,c,dist = q.popleft()
                rooms[r][c] = min(dist,rooms[r][c])
                if r+1< n and rooms[r+1][c]!=-1 and (r+1,c) not in seen:
                    q.append((r+1,c,dist+1))
                    seen.add((r+1,c))
                    # rooms[r+1][c] = dist+1
                if c + 1< m and rooms[r][c+1]!=-1  and (r,c+1) not in seen:
                    q.append((r,c+1,dist+1))
                    seen.add((r,c+1))
                    # rooms[r][c+1] = dist+1
                if r-1>= 0 and rooms[r-1][c]!=-1  and (r-1,c) not in seen:
                    q.append((r-1,c,dist+1))
                    rooms[r-1][c] = dist+1
                    seen.add((r-1,c))
                if c-1>= 0 and rooms[r][c-1]!=-1  and (r,c-1) not in seen:
                    q.append((r,c-1,dist+1))
                    seen.add((r,c-1))
                    # rooms[r][c-1] = dist+1
        

                
