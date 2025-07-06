class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        q.append((sr,sc))
        start = image[sr][sc]
        visit = set()
        while q:
            r,c = q.popleft()
            visit.add((r,c))
            image[r][c] = color
            if r+1 < len(image) and (r+1,c) not in visit and image[r+1][c]==start:
                q.append((r+1,c))
            if c+1 < len(image[0]) and (r,c+1) not in visit and image[r][c+1]==start:
                q.append((r,c+1))
            if r-1>=0 and (r-1,c) not in visit and image[r-1][c]==start:
                q.append((r-1,c))
            if c-1>=0 and (r,c-1) not in visit and image[r][c-1]==start:
                q.append((r,c-1))
        
        return image
